import os
import time

import xmltodict
from flask import Flask, request

from bot import Chatbot

os.environ['GPT_ENGINE'] = 'text-davinci-003'

app = Flask(__name__)

def parse_msg(xml: bytes) -> dict:
    return xmltodict.parse(xml).get('xml')

def pack_msg(reply_info: dict, msg: str) -> str:
    resp_dict = {
        "xml": {
            'ToUserName': reply_info.get('FromUserName'),
            'FromUserName': reply_info.get('ToUserName'),
            'CreateTime': int(time.time()),
            'MsgType': 'text',
            'Content': msg
        }
    }
    return xmltodict.unparse(resp_dict)

@app.route("/wechat", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # 用于验证
        return request.args.get('echostr', type=int, default='')

    def answer(ask: str) -> str:
        response = chatbot.ask(ask, temperature=0.5)
        print("Ask: " + ask)
        print("ChatGPT: " + response["choices"][0]["text"])
        return response["choices"][0]["text"]

    if not request.data:
        return '', 403

    reply_info = parse_msg(request.data)

    msg = answer(reply_info['Content'])

    return pack_msg(reply_info, msg)


if __name__ == '__main__':
    chatbot = Chatbot(api_key='')
    app.run(host='0.0.0.0', port=80, debug=True)
