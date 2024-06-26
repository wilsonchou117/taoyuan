from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

# 常見問答表
faq = {
    '貼圖': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
    '美股即時報價': TemplateSendMessage(
        alt_text='Carousel template2',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    title='美股選單一',
                    text='點選下方按鈕查詢美股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢蘋果',
                            text='AAPL'
                        ),
                        MessageAction(
                            label='查詢谷歌',
                            text='GOOGL'
                        ),
                        MessageAction(
                            label='查詢微軟',
                            text='MSFT'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    title='美股選單二',
                    text='點選下方按鈕查詢美股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢輝達',
                            text='NVDA'
                        ),
                        MessageAction(
                            label='查詢超微',
                            text='AMD'
                        ),
                        MessageAction(
                            label='查詢特斯拉',
                            text='TSLA'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    title='美股選單三',
                    text='點選下方按鈕查詢美股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢亞馬遜',
                            text='AMZN'
                        ),
                        MessageAction(
                            label='查詢臉書',
                            text='META'
                        ),
                        MessageAction(
                            label='查詢摩根大通銀行',
                            text='JPM'
                        )
                    ]
                )
            ]
        )
    ),
    '台股即時報價': TemplateSendMessage(
        alt_text='Carousel template2',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    title='台股選單一',
                    text='點選下方按鈕查詢國小課程報價',
                    actions=[
                        MessageAction(
                            label='查詢台積電',
                            text='台積電'
                        ),
                        MessageAction(
                            label='查詢大立光',
                            text='大立光'
                        ),
                        MessageAction(
                            label='查詢聯發科',
                            text='聯發科'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    title='台股選單二',
                    text='點選下方按鈕查詢台股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢和泰車',
                            text='和泰車'
                        ),
                        MessageAction(
                            label='查詢國巨',
                            text='國巨'
                        ),
                        MessageAction(
                            label='查詢聯詠',
                            text='聯詠'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    title='台股選單三',
                    text='點選下方按鈕查詢台股即時報價',
                    actions=[
                        MessageAction(
                            label='查詢群聯',
                            text='群聯'
                        ),
                        MessageAction(
                            label='查詢瑞昱',
                            text='瑞昱'
                        ),
                        MessageAction(
                            label='查詢環球晶',
                            text='環球晶'
                        )
                    ]
                )
            ]
        )
    ),
    '視聽觀看': TextSendMessage(
        text="https://docs.google.com/spreadsheets/d/1qbuEm3QcCdNaFr6Jss2I0SjPWxW-jPrb30Pd-xaMH-I/edit#gid=924794706"
    ),
    '匯款資訊': ImageSendMessage(
        original_content_url='https://i.postimg.cc/jqgrNvrY/c3.png',
        preview_image_url='https://i.postimg.cc/jqgrNvrY/c3.png'
    ),
    '國小課程查詢': ImageSendMessage(
        original_content_url='https://i.postimg.cc/85pqffKC/c1.jpg',
        preview_image_url='https://i.postimg.cc/85pqffKC/c1.jpg'
    ),
    '國中課程查詢': ImageSendMessage(
        original_content_url='https://i.postimg.cc/D0mHBkKk/c2.jpg',
        preview_image_url='https://i.postimg.cc/D0mHBkKk/c2.jpg'
    ),
    '課程報價': ImageSendMessage(
        original_content_url='https://i.postimg.cc/gc3sY6pp/4.jpg',
        preview_image_url='https://i.postimg.cc/gc3sY6pp/4.jpg'
    ),
    '預約視聽': TextSendMessage(
        text="https://calendar.google.com/calendar/u/0/r?hl=zh-TW"
    ),
    '預約畫位': TextSendMessage(
        text="https://docs.google.com/spreadsheets/d/18o1G9n05nC3cSrosfvnM99IEyg1V7jHJtm-CRmd2a_s/edit?pli=1#gid=0"
    ),
    '聯絡資訊': TextSendMessage(
        text="電話:(03)-3311833,地址:桃園市桃園區民權路6號7樓"
    ),
    '美股買賣點': TextSendMessage(text='請問您想詢問哪家公司？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="蘋果公司", text="蘋果")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="谷歌", text="谷歌")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="微軟", text="微軟")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="臉書", text="臉書")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="輝達", text="輝達")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="超微", text="超微")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="特斯拉", text="特斯拉")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="亞馬遜", text="亞馬遜")
                              )
                             ])
                          ),
    '台股買賣點': TextSendMessage(text='請問您想詢問哪家公司？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="台積電", text="TSMC")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="鴻海", text="Foxconn")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="聯發科", text="MediaTek")
                              )
                          ])
                          ),
    '蘋果': TextSendMessage(
        text="蘋果 2024/2/29 買點:172，賣點198"
    ),
    '谷歌': TextSendMessage(
        text="谷歌 2024/2/29 買點:128，賣點153"
    ),
    '微軟': TextSendMessage(
        text="微軟 2024/2/29 買點:398，賣點419"
    ),
    '臉書': TextSendMessage(
        text="臉書 2024/2/29 買點:460，賣點498"
    ),
    '輝達': TextSendMessage(
        text="輝達 2024/2/29 買點:725，賣點825"
    ),
    '超微': TextSendMessage(
        text="超微 2024/2/29 買點:167，賣點188"
    ),
    '特斯拉': TextSendMessage(
        text="特斯拉 2024/2/29 買點:189，賣點214"
    ),
    '亞馬遜': TextSendMessage(
        text="亞馬遜 2024/2/29 買點:168，賣點179"
    ),
    'TSMC': TextSendMessage(
        text="台積電 2024/3/1 買點:667，賣點699"
    ),
    'Foxconn': TextSendMessage(
        text="鴻海 2024/3/1 買點:101，賣點103"
    ),
    'MediaTek': TextSendMessage(
        text="聯發科 2023/3/1 買點:945，賣點996"
    ),
    '分校地址': LocationSendMessage(
        title='my location',
        address='Taoyuan',
        latitude=24.98998,
        longitude=121.31184
    ),
    '查詢匯率': TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 匯率選單一圖片網址
                    thumbnail_image_url='https://picsum.photos/id/352/900/400',
                    title='匯率選單一',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢美金',
                            text='美金'
                        ),
                        MessageAction(
                            label='查詢港幣',
                            text='港幣'
                        ),
                        MessageAction(
                            label='查詢英鎊',
                            text='英鎊'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單二圖片網址
                    thumbnail_image_url='https://picsum.photos/id/364/900/400',
                    title='匯率選單二',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢澳幣',
                            text='澳幣'
                        ),
                        MessageAction(
                            label='查詢加拿大幣',
                            text='加拿大幣'
                        ),
                        MessageAction(
                            label='查詢新加坡幣',
                            text='新加坡幣'
                        )
                    ]
                ),
                CarouselColumn(
                    # 匯率選單三圖片網址
                    thumbnail_image_url='https://picsum.photos/id/355/900/400',
                    title='匯率選單三',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢瑞士法郎',
                            text='瑞士法郎'
                        ),
                        MessageAction(
                            label='查詢日圓',
                            text='日圓'
                        ),
                        MessageAction(
                            label='查詢瑞典幣',
                            text='瑞典幣'
                        )
                    ]
                )
                
            ]
        )
    )
}












# 主選單
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                # 卡片一圖片網址
                thumbnail_image_url='https://i.postimg.cc/VL8DG5v4/FA57-BC5-A-CF4-F-4-FF7-BA76-0-C4-D442-EDEA1.jpg',
                title='課程查詢及報價',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='國小課程查詢',
                        text='國小課程查詢'
                    ),
                    MessageAction(
                        label='國中課程查詢',
                        text='國中課程查詢'
                    ),
                    MessageAction(
                        label='課程報價',
                        text='課程報價'
                    )
                ]
            ),
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url='https://i.postimg.cc/VL8DG5v4/FA57-BC5-A-CF4-F-4-FF7-BA76-0-C4-D442-EDEA1.jpg',
                title='視聽觀看預約畫位',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='視聽觀看',
                        text='視聽觀看'
                    ),
                    MessageAction(
                        label='預約畫位',
                        text='預約畫位'
                    ),
                    MessageAction(
                        label='預約視聽',
                        text='預約視聽'
                    )
                ]
            ),
            CarouselColumn(
                # 卡片二圖片網址
                thumbnail_image_url='https://i.postimg.cc/VL8DG5v4/FA57-BC5-A-CF4-F-4-FF7-BA76-0-C4-D442-EDEA1.jpg',
                title='匯款資訊分校地址',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='匯款資訊',
                        text='匯款資訊'
                    ),
                    MessageAction(
                        label='分校地址',
                        text='分校地址'
                    ),
                    MessageAction(
                        label='聯絡資訊',
                        text='聯絡資訊'
                    )
                ]
            )
        ]
    )
)