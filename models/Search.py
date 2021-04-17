from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#相当于一个小的连接池
class Search(db.Model):

    pass
