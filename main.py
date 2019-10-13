from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)

import os

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.environ['eLZTT6uLPSlHfhxgmCO+QspYKk77gWRQumK6N4xvpiK1I00ID1yOh8KgvNmJqMbemnJ9uQrzE2QdRTHV927nMapipSelbSDKfE672LBvhvoG9yLKI3TAKwQoVoXoj+l1AW41Mebp4gNhr28QZZ2T7QdB04t89/1O/w1cDnyilFU=']
LINE_CHANNEL_SECRET = os.environ['7e1a4872c937789c5a8003c2d51d5add']

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='「' + event.message.text + '」って何？')
     )

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)