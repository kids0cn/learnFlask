'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 16:38:16
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-15 16:43:28
FilePath: /learnFlask/3_鱼书/app/models/user.py
Description: 



Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from app.models.base import Base
from sqlalchemy import Column,Integer,String,Boolean,Float
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.spider.yushu_book import YuShuBook
from app.models.gift import Gift
from app.models.wish import Wish


class User(Base,UserMixin):
    __tablename__ = 'user' # 决定了写入数据库的表明
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
    __password = Column('password',String(128),nullable=False)  # 数据库中字段名称为password，模型中字段名称为__password
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,raw):
        self.__password = generate_password_hash(raw)  # 加密之后存储在数据库中
    
    def check_password(self,raw):
        return check_password_hash(self.__password,raw)
    
    def can_save_to_list(self,isbn):
        # 首先判断这个书是否合法
        # 其次判断这个书是否在赠送清单和心愿清单中
        if isbn_or_key != 'isbn':
            return False #不允许添加图书
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first: # 如果没有这本书，数据库中没有这本书
            return False
        # 不允许一个用户同时赠送多本相同的图书
        # 一个用户不可能同时既想赠送又想收藏一本书
        # 既不在赠送清单，又不在心愿清单才能添加
        gifting = Gift.query.filter_by(uid=self.id,isbn=isbn).first()
        wishing = Wish.query.filter_by(uid=self.id,isbn=isbn).first()
        if not gifting and not wishing:
            return True
        else:
            return False
        


        
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))