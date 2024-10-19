'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 17:17:19
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-14 20:46:37
FilePath: /learnFlask/3_鱼书/app/forms/auth.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from wtforms import Form,StringField
from wtforms.validators import DataRequired,Length,Email,ValidationError
from app.models.user import User



class RegsiterForm(Form):
    email = StringField(validators=[DataRequired(message='电子邮箱不能为空'),Length(8,64),Email(message='电子邮箱不符合规范')])
    password = StringField(validators=[DataRequired(message='密码不能为空'),Length(6,32)])
    nickname = StringField(validators=[DataRequired(message='昵称不能为空'),Length(2,10,message='昵称长度必须在2到10个字符之间')])


    # 自定义业务校验器，比如Email不能重复
    def validate_email(self,field): # 写的Email。则校验器自己就知道对email进行校验
        # db session
        if User.query.filter_by(email=field.data).first():
            # User.query 是 SQLAlchemy 提供的查询接口，用于对 User 模型进行数据库查询。
            raise ValidationError('电子邮箱已被注册')
        

    def validata_nickname(self,field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('昵称已存在')
        

class LoginForm(Form):
    email = StringField(validators=[DataRequired(message='电子邮箱不能为空'),Length(8,64),Email(message='电子邮箱不符合规范')])
    password = StringField(validators=[DataRequired(message='密码不能为空'),Length(6,32)])
    nickname = StringField(validators=[DataRequired(message='昵称不能为空'),Length(2,10,message='昵称长度必须在2到10个字符之间')])

