'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 16:38:28
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-14 16:57:11
FilePath: /learnFlask/3_鱼书/app/models/base.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,SmallInteger

db = SQLAlchemy()

class Base(db.Model):
    status = Column(SmallInteger,default=1)