'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 16:38:16
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-14 16:42:24
FilePath: /learnFlask/3_鱼书/app/models/user.py
Description: 



Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from app.models.base import db
from sqlalchemy import Column,Integer,String,Boolean,Float

class User(db.Model):
    id = Column(Integer,primary_key=True)
    nickname = Column(String(24),nullable=False)
    phone_number = Column(String(18),unique=True)
    email = Column(String(50),unique=True,nullable=False)
    confirmed = Column(Boolean,default=False)
    beans = Column(Float,default=0)
    send_counter = Column(Integer,default=0)
    receive_counter = Column(Integer,default=0)
    wx_open_id = Column(String(50),unique=True,nullable=False)
    wx_name = Column(String(32))
    
    