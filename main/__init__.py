from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://users_kze4_user:oJxCT7skCR79rqg7nud8ApS2ZqhOigEn@dpg-cibdsod9aq03rjn5ski0-a.oregon-postgres.render.com/users_kze4"
db = SQLAlchemy(app)

from main import routes
from main import models
from main import templates