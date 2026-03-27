from config import db, login_manager
from flask_login import UserMixin
    
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.query.get(int(user_id))

def getUserByEmail(email):
    return User.query.filter_by(email=email).first()