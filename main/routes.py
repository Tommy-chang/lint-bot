from main import mathe
from flask import Flask, request, abort,render_template
from main import app
from main import db
from main.models import user_info
from main.lists import *
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import random
import re 
from main.lists import *
from main.template import *
import main.mathe
from flask_sqlalchemy import SQLAlchemy
from main import routes



#======這裡是呼叫的檔案內容=====
from main.message import *
from main.Function import *
#======這裡是呼叫的檔案內容=====




#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========



static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('dh2uBmeU9i5d2tI3+3txaxM35eGR+tRTb47qKvHx5SIalG+zjJLK0EDox2ytJEh7pXQ5OXNhyVJVyQsphPEs4ZQdZTGYhGWKnPn1TAXsG7SR35cRSnio9FZ13NJzopeQw2lOMmzXK51fidoy4U/3ygdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2e2bc01c7524809d68a04778f7ee1330')

@app.route("/")
def home_page():
    return render_template("home_page.html")


# 監聽所有來自 /callback 的 Post Request
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


    

#加好友
@handler.add(FollowEvent)
def sendMessage(event):
    user_id = event.source.user_id
    print(user_id)
    profile = line_bot_api.get_profile(user_id)
    user_name = profile.display_name
    pic_url = profile.picture_url
    status = profile.status_message
    message = TextSendMessage(text =f"你好, 非常高興能夠成為你的好友, {user_name} :) \n 需要幫助的話, 可輸入指令robot.help")
    line_bot_api.reply_message(event.reply_token, message)
    if user_info.query.filter(user_info.user_id==user_id).all() !=True:
        db.create_all()
        user = user_info(user_id=user_id, username=user_name, pic_url=pic_url, status=status)
        db.session.add(user)
        db.session.commit()


#新的成員進到群組
@handler.add(MemberJoinedEvent)
def member_joind(event):
    print(event)
    print(event.joined.members[0])
    user_id = event.joined.members[0].user_id
    group_id = event.source.group_id
    summary = line_bot_api.get_group_summary(group_id)
    group_name = summary.group_name
    profile = line_bot_api.get_profile(user_id)
    pic_url = profile.picture_url
    status = profile.status_message
    user_name = profile.display_name
    message = TextSendMessage(text="歡迎"+ user_name +"來到" + group_name + "!")
    line_bot_api.reply_message(event.reply_token, message)
    if user_info.query.filter(user_info.user_id==user_id).all() !=True:
        db.create_all()
        user = user_info(user_id=user_id, username=user_name, pic_url=pic_url, status=status)
        db.session.add(user)
        db.session.commit()

@handler.add(MemberLeftEvent)
def member_left(event):
    print(event.left.members[0])
    user_id = event.left.members[0].user_id
    group_id = event.source.group_id
    profile = line_bot_api.get_profile(user_id)
    user_name = profile.display_name
    summary = line_bot_api.get_group_summary(group_id)
    group_name = summary.group_name
    message = TextSendMessage(text=f"{user_name}離開了" + group_name + "!")
    line_bot_api.push_message(group_id,message)
   


@handler.add(JoinEvent)
def joined(event):
    group_id = event.source.group_id
    # member_ids_res = line_bot_api.get_group_member_ids(group_id)
    summary = line_bot_api.get_group_summary(group_id)
    # print(member_ids_res.member_ids)
    group_name = summary.group_name
    message = TextSendMessage(text= "Hi everyone in the" + " '" + str.upper(group_name) + "' " +"!")
    line_bot_api.reply_message(event.reply_token, message)




# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    profile = line_bot_api.get_profile(user_id)
    user_name = profile.display_name
    pic_url = profile.picture_url
    status = profile.status_message
    msg =event.message.text
    print(event)
    print(user_id)
    # line_bot_api.push_message("Uab668705725086bddb48da2453367cac", TextSendMessage(text="hi"))

    if user_info.query.filter(user_info.user_id==user_id).first() ==None:
        db.create_all()
        user = user_info(user_id=user_id, username=user_name, pic_url=pic_url, status=status)
        db.session.add(user)
        db.session.commit()
        message = TextSendMessage(text="try again please")
        line_bot_api.reply_message(event.reply_token, message)
        
    elif "robot.send_message" in msg:
        if event.source.user_id == "Uab668705725086bddb48da2453367cac":
            message = TextSendMessage(
                text=msg.replace("robot.send_message", "")
            )
            for i in user_list:
                print(i)
                line_bot_api.push_message(str(i[0]), message)
        else:
            message = TextSendMessage(text="不要再試了！")
            line_bot_api.reply_message(event.reply_token, message)

    elif "更新資料" in msg:
        user = user_info.query.filter(user_info.user_id==user_id).first()
        user.user_id, user.username, user.status, user.pic_url=user_id, user_name, status, pic_url
        db.session.commit()
    elif "個人資料" in msg:
        message = TextSendMessage(text=str(user_info.query.filter(user_info.user_id==user_id).all()))
        line_bot_api.reply_message(event.reply_token, message)
    elif "robot.who" in msg:
        message = imagemap_message()
        line_bot_api.reply_message(event.reply_token,message)
    elif '最新活動訊息' in msg:
        message = buttons_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '註冊會員' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '旋轉木馬' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif 'robot.help' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif "新聞" in msg:
        msg = msg.replace("新聞", "")
        try:
            times = re.findall(r"[0-9]+",msg)
            type = msg.replace(str(times[0]), "")
            message = get_news(int(times[0]), type)
            line_bot_api.reply_message(event.reply_token, message)
        except:
            message = get_news()
            line_bot_api.reply_message(event.reply_token, message)

    elif "robot.search" in msg:
        try:
            message=search(msg)
            line_bot_api.reply_message(event.reply_token, message)
        except:
            message = TextSendMessage(text="無搜尋結果")
            line_bot_api.reply_message(event.reply_token, message)
    
    #compute
    elif "robot.equation" in msg:
        message = mathe.equation(msg)
        line_bot_api.reply_message(event.reply_token, message)

    elif "robot.poly" in msg:
        message = mathe.polyn(msg)
        line_bot_api.reply_message(event.reply_token, message)

    elif "robot.plus" in msg:
        message_list = re.findall(r"[0-9]+",msg)
        message = TextSendMessage(text = float(message_list[0])+float(message_list[1]))
        line_bot_api.reply_message(event.reply_token, message)
    elif "robot.minus" in msg:
        message_list = re.findall(r"[0-9]+",msg)
        message = TextSendMessage(text = float(message_list[0])-float(message_list[1]))
        line_bot_api.reply_message(event.reply_token, message)
    elif "robot.multiply" in msg:
        message_list = re.findall(r"[0-9]+",msg)
        message = TextSendMessage(text = float(message_list[0])*float(message_list[1]))
        line_bot_api.reply_message(event.reply_token, message)
    elif "robot.divide" in msg:
        message_list = re.findall(r"[0-9]+",msg)
        message = TextSendMessage(text = float(message_list[0])/float(message_list[1]))
        line_bot_api.reply_message(event.reply_token, message)
    elif   "robot.AS"  in msg:
        message_list = re.findall(r"[0-9]+",msg)
        message = TextSendMessage(text = mathe.normal(int(message_list[0]),int(message_list[1]),int(message_list[2])))
        line_bot_api.reply_message(event.reply_token, message)
    
    #other replies
    elif   int(len(msg))>=50  :
        message = TextSendMessage(text="不要吵!!")
        line_bot_api.reply_message(event.reply_token, message)
    elif  "..."  in msg:
        message = TextSendMessage(text="你無言了吧")
        line_bot_api.reply_message(event.reply_token, message)
    elif  "你好爛" in str.lower(msg):
        message = TextSendMessage(text="至少比" + user_name +"好")
        line_bot_api.reply_message(event.reply_token, message)   
    elif any(word in msg for word in words):
        option = random.choice(options)
        message = TextSendMessage(text=option)
        line_bot_api.reply_message(event.reply_token, message)
    elif   "笨蛋"  in msg:
        message = TextSendMessage(text=user_name + "才是大笨蛋")
        line_bot_api.reply_message(event.reply_token, message)
    elif   "who is robot"  in str.lower(msg):
        message = TextSendMessage(text="我是超強機器人,歡迎加我好友,我會幫你解決問題喔!")
        line_bot_api.reply_message(event.reply_token, message)
    
    else:
        try:
            message = TextSendMessage(text=msg)
            line_bot_api.reply_message(event.reply_token, message)
        except:
            message = TextSendMessage(emojis=msg)
            line_bot_api.reply_message(event.reply_token, message)