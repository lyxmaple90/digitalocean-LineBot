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
        current_datetime = GetJPDateTime()  # 獲得當前日期和時間 "YYYY-MM-DD HH:MM:SS"
        current_date = current_datetime.split(" ")[0]  # 獲得當前日期 "YYYY-MM-DD"
        current_time = current_datetime.split(" ")[1]  # 獲得當前時間 "HH:MM:SS"
        
        # 檢查是否為每年的11月24日並且時間為00:00:00
        if current_date[-5:] == "11-24" and current_time == "00:00:00":
            onemessage = TextSendMessage(
                text="お誕生日おめでとう!!"
            )
            line_bot_api.broadcast(onemessage)
            # 等待24小時到下一天，因為我們不想在同一天重複發送訊息
            time.sleep(86400)  
        else:
            # 如果不是11月24日午夜00:00:00，則稍微暫停一下再次檢查
            time.sleep(5)  # 每5秒檢查一次，您可以根據需要調整這個時間



onemessage = TextSendMessage(
                text="テストです(無視してください)"
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
    

