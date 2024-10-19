'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-15 11:37:46
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-15 11:39:21
FilePath: /learnFlask/3_鱼书/app/models/wish.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''


from app.models.base import Base
from sqlalchemy import Column,Integer,String,Boolean,Float,ForeignKey
from sqlalchemy.orm import relationship

class Wish(Base):
    id = Column(Integer,primary_key=True)
    launched = Column(Boolean,default=False) # 是否被赠送出去
    user = relationship('User') # 关联User表
    isbn = Column(String(13),nullable=False)
    uid = Column(Integer,ForeignKey('user.id'))
    # 数据库里没有保存数据信息，所以这里暂时注释掉，保留isbn
    # book = relationship('Book')
    # bid = Column(Integer,ForeignKey('book.id'))