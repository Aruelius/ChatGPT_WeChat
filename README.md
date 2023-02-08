# ChatGPT_WeChat
基于 ChatGPT 回复的极简微信公众号机器人

## 安装依赖
pip install revChatGPT xmltodict flask

## 使用说明
1. 首先需要去微信公众号后台配置接口，[具体文档看这里](https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Access_Overview.html)。其中 URL 填接口地址，如果是本项目不修改直接运行，那就是服务器 IP + /wechat（示例：http://192.168.1.1/wechat），Token 随便填，AES KEY 点随机生成，先**不点**提交。
2. 去 `app.py` 中填写好 OpenAI 的 API KEY，运行本项目 `python app.py` 后，点提交。这样就配置好了接口。
3. 发消息给自己的公众号，看看是否有回应。

## 注意
1. 极简 Bot，没做别的控制，注意别被滥用。
2. 如果我没猜错的话，所有的用户都是共用一个 conversion
3. 微信公众号被动回复消息文档：[点击这里](https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Passive_user_reply_message.html)
4. 代码中的 GPT_ENGINE 应该指的是 model，我这里用的是 `text-davinci-003`，这是个**付费模型**，测试下来，这个模型回复速度才能达到微信公众号要求的 5s 限制，偶尔会有超时，但是大部分都正常。如果使用免费的模型，需要 15s 反应时间，可能一直会提示 `该公众号提供的服务出现故障，请稍后再试`。
