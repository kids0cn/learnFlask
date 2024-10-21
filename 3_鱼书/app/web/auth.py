'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 14:55:25
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-18 16:03:25
FilePath: /learnFlask/3_鱼书/app/web/auth.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from . import web 
from flask import render_template,request,redirect,url_for
from app.forms.auth import RegsiterForm,LoginForm
from app.models.user import User
from app.models.base import db
from flask import flash
from flask_login import login_user


@web.route('/register',methods = ['get','post']) # 让这个视图函数支持get和post请求
def register():
    form = RegsiterForm(request.form)
    if request.method == 'POST':
        print("Formdata",request.form)
    print(form.data)
    if request.method == 'POST' and form.validate(): # 如果请求方式是post，并且表单验证通过
        # 要操作数据库
        print("0000000验证成功")
        with db.auto_commit():
            print("++++++++++++++++++++")
            print("马上创建新的user表了")
            user = User()
            user.set_attrs(form.data)
            db.session.add(user)
            print("++++++++++++")
            print("创建完成了")
        # 注册成功后，跳转到登录页面
        redirect(url_for('web.login'))
    # 如果表单验证不通过，此时form.data里不仅包含了错误信息，还有用户已经输入的数据

    return render_template('auth/register.html',form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        # 用户存在，则比对密码
        if user and user.check_password(form.password.data):
            # 登陆成功之后，就要发放和管理令牌，太麻烦了，用flask-login插件
            login_user(user) # 这个函数要求我们在user模型里写一个固定的函数get_id()用来返回标识用户身份的东西
            # 在初始化login插件时，制定了app的登录位置，所有要授权的网站，都会重定向到登录页面
            # 位置在create_app里
            # 登录成功的页面，则需要返回正常的位置
            #return redirect(url_for('web.index'))
            next = request.args.get('next') # 获取next参数
            if not next or not next.startswith('/'): #next不是以斜杠开头，强制到首页，主要是为了防止next是其他网站的链接
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('密码错误')
    return render_template("auth/login.html",form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
