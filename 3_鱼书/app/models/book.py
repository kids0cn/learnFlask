'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-02 19:58:43
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-08 21:38:44
FilePath: /learnFlask/3_鱼书/app/models/book.py
Description:

# 业务模型，code驱动的数据库，即写完业务代码后，再写数据库模型，自动映射数据库
# Flask_SQLAlchemy 是 Flask 的 ORM 框架 
# 之前数据驱动的模型，是先要思考数据库的表结构，相互之间什么关系。但是code first的设计
则是将数据库单纯看做数据存储的位置，它的表关系由业务来决定

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''





from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String

db = SQLAlchemy()

class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True) # 
    title = Column(String(50),nullable=False)
    author = Column(String(30),default='未名')
    binding = Column(String(20))  # 装帧格式 精装 平装
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(Integer)
    isbn = Column(String(15),nullable=True,unique=True) # isbn不重复
    summary = Column(String(1000))
    image = Column(String(50))
    