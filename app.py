from distutils.log import debug
from main import app
from main.lists import *
import random
from apscheduler.schedulers.blocking import BlockingScheduler
from app import *
import datetime
from linebot.models import *
from apscheduler.schedulers.blocking import BlockingScheduler
from main.routes import line_bot_api


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    sched = BlockingScheduler() 



    # @sched.scheduled_job("cron", day_of_week = "mon-sun", hour="21", minute="30")
    # def scheduled_job():
    #     print(datetime.datetime.now().ctime())
    #     print("hi")
    #     for i in user_list:
    #         word = random.choice(n_send_options)
    #         line_bot_api.push_message(i, TextSendMessage(text=word))

    # @sched.scheduled_job("cron", day_of_week = "mon-sun", hour="7", minute="00")
    # def scheduled_job():
    #     print(datetime.datetime.now().ctime())
    #     print("hi")
    #     for i in user_list:
    #         word = random.choice(m_send_options)
    #         line_bot_api.push_message(i, TextSendMessage(text=word))

    
    app.run(host="0.0.0.0", port=port, debug=True)
    sched.start()
