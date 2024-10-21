'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 16:38:28
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-21 17:17:56
FilePath: /learnFlask/3_鱼书/app/models/base.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask_sqlalchemy import SQLAlchemy  as  _SQLAlchemy
from sqlalchemy import Column,SmallInteger,Integer
from contextlib import contextmanager
from datetime import datetime




class Query(_SQLAlchemy):
    def filter_by(self, **kwargs):
        # 就是为了加上status=1的，因为是采用的是假删除，所以要把这个都默认加上
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)





class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
        

db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    # 把子模型都需要有参数放到基类里
    __abstract__ = True # 定义为抽象类
    status = Column(SmallInteger,default=1)
    create_time = Column('create_time',Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self,attrs_dict):
        # 遍历传进来的字典，把同名的属性赋值给模型
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id': 
                setattr(self,key,value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
        


