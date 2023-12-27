from linebot import  LineBotApi
import time
from GetJPTime import GetJPTime
from GetJPDateTime import GetJPDateTime
import threading


line_bot_api = LineBotApi('61r/mO0+uhN0io7/R0OnGZb5m3O7ED0Qr+s9xsijsYfvbRD+CdLmnasEwxxylaT5oGtOTOYdHNY9ZsMcsTfdcKIs18fsfSk+MXNgp/FI02m2yS8PvHUm3LR4x8mzVJqxzqqagFLQC145teKSw6+1mQdB04t89/1O/w1cDnyilFU=')
from linebot.models import TemplateSendMessage, MessageTemplateAction, ConfirmTemplate,TextSendMessage
message = TemplateSendMessage(
            alt_text="薬は、飲みましたか？",
            template = ConfirmTemplate(
                text="薬は、飲みましたか？",
                actions=[
                    MessageTemplateAction(
                        label='飲んだー',
                        text="飲んだー"
                    ),
                    MessageTemplateAction(
                        label='まだー',
                        text="まだー"
                    )
                ]
            )
        )


def f2():
    while True:
        if GetJPDateTime() == "2023-11-24 00:00:00":   
            onemessage = TextSendMessage(
                text="お誕生日おめでとう!!"
            )
            time.sleep(1)
            line_bot_api.broadcast(onemessage)
            time.sleep(1)
            break


onemessage = TextSendMessage(
                text="テストです"
            )
time.sleep(1)
line_bot_api.broadcast(onemessage)
t = threading.Thread(target=f2)  #建立執行緒
t.start()            


while True:

    

    if GetJPTime() == "09:00:00" or GetJPTime() == "21:00:00":
        time.sleep(1)
        line_bot_api.broadcast(message)
        time.sleep(1)
    

