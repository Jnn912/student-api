from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# 初始化Flask应用
app = Flask(__name__)
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)

# 导入路由和模型
from app import routes, models

# 创建数据库表
with app.app_context():
    db.create_all()