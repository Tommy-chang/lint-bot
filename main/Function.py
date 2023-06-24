#這個檔案的作用是：建立功能列表

#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================

#以下是本檔案的內容本文

#1.建立旋轉木馬訊息，名為function_list(未來可以叫出此函數來使用)
#function_list的括號內是設定此函數呼叫時需要給函數的參數有哪些

def function_list():
    message = TemplateSendMessage(
        alt_text='功能列表',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url="https://i.imgur.com/F2rAQ0s.jpg?1",
                    title='加和減',
                    text='robot.plus/minus n1 n2',
                    actions=[
                        MessageTemplateAction(
                            label='加的範例',
                            text='robot.plus 1 3'
                        ),
                        MessageTemplateAction(
                            label="減的範例",
                            text="robot.minus 5 3"
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://i.imgur.com/F2rAQ0s.jpg?1",
                    title='乘和除',
                    text='robot.multiply/divide n1 n2',
                    actions=[
                        MessageTemplateAction(
                            label='乘的範例',
                            text='robot.multiply 13 34'
                        ),
                        MessageTemplateAction(
                            label="除的範例",
                            text="robot.divide 10 5"
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://i.imgur.com/F2rAQ0s.jpg?1",
                    title='等差數列, 一元多次方程式',
                    text='robot.AS a1 an d/equation算式(不可用等號, 算式值須等於零)',
                    actions=[
                        MessageTemplateAction(
                            label='等差數列的範例',
                            text='robot.AS 1 100 1'
                        ),
                        MessageTemplateAction(
                            label="一元多次方程式的範例",
                            text="robot.equation x-1+3"
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://i.imgur.com/F2rAQ0s.jpg?1",
                    title="多項式",
                    text="robot.poly 算式",
                    actions=[
                        MessageTemplateAction(
                            label="多項式的範例",
                            text="robot.poly (x-2)**2+(x+3)*3"
                        ),
                        MessageTemplateAction(
                            label="多項式的範例",
                            text="robot.poly (x+3)**2+(y+4)**2"
                        )
                    ]

                ),
                CarouselColumn(
                    thumbnail_image_url="https://i.imgur.com/F2rAQ0s.jpg?1",
                    title='搜尋新聞',
                    text='新聞 數量 種類',
                    actions=[
                        MessageTemplateAction(
                            label='範例',
                            text='新聞 3 國際'
                        ),
                        URITemplateAction(
                            label='新聞來源:聯合新聞網',
                            uri='https://udn.com/news/index'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url="https://i.imgur.com/F2rAQ0s.jpg?1",
                    title='檢視個人資料及更新',
                    text='個人資料',
                    actions=[
                        MessageTemplateAction(
                            label='檢視範例',
                            text='個人資料'
                        ),
                        MessageTemplateAction(
                            label="更新範例",
                            text="更新資料"
                        )
                    ]
                ),
            ]
        )
    )
    return message