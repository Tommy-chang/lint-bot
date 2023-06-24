#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import urllib.request as req
from bs4 import BeautifulSoup
import random
from urllib.parse import quote
#關於LINEBOT聊天內容範例
def get_news(times=1, type="index"):
    if type == "   國際":
        type = type.replace("國際", "cate/2/7225")
    elif type == "   國內":
        type = type.replace("國內", "cate/2/6649")
    else:
        type = "index"

    url = f"https://udn.com/news/{type}"
    inter = req.Request(url, headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    })
    with req.urlopen(inter) as response:
        data =response.read().decode("utf-8")
    data = BeautifulSoup(data, "html.parser")
    news = data.find_all("div", class_= "story-list__text")
    x = random.randint(1, 5)
    a = ""
    for new in news[x:x+times]:
        a+= "\n"+"---" + new.p.string + "\n" + "\n" + "查看完整文章--->" + new.a["href"] + "\n" + "(有時候可能是業配, 我也沒辦法QQ)"
    message = TextSendMessage(text=a)
    return message


def search(inner):
    iner=inner.replace("robot.search","")
    ok=quote(iner)
    url="https://zh.wikipedia.org/wiki/"+ok
    Inter=req.Request(url,headers={
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    })
    with req.urlopen(Inter) as response:
        data=response.read().decode("utf-8")
    root=BeautifulSoup(data,"html.parser")
    article=root.find("p")#"div", class_="mw-parser-output"
    message=TextSendMessage(text=str(article))
    return message




    






