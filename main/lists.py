from main.models import user_info
from main import db
words = ["wtf", "幹", "機掰"]
options = [
    "不要罵髒話",
    "DO NOT SAY BAD WORDS!!!"
]
user_list = db.session.query(user_info.user_id).all()
n_send_options = ["Hi there, it is 9:30, time to sleep! zzz", "The robot is too quiet? Never say that again.", "Too boring? Then chat with me!"]
m_send_options = ["Good morning!", "It is beginning of a wonderful day!"]