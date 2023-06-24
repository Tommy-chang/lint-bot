from main import db
class user_info(db.Model):
    user_id = db.Column(db.String(length=100), primary_key=True)
    username = db.Column(db.String(length=100), nullable=False)
    pic_url = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(length=100))
    
    def __repr__(self):
        return f"user_info:\n user_id:{self.user_id} \n username:{self.username} \n picture_url:{self.pic_url} \n status:{self.status}"