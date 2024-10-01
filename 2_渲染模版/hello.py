'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-30 17:42:22
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-01 14:31:45
FilePath: /learnFlask/2_渲染模版/hello.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask import Flask,render_template,make_response

# 指定模版文件夹
app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usr/<name>')
def user(name):
    return render_template('user.html',name=name) # 模版名user.html，渲染变量name

class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

@app.route('/variable')
def variable():
    hobby = 'game'
    user = User(username='kids0cn',email='kids0cn@gmail.com')
    person = {
        'name':'tom',
        'age':20
    }
    return render_template('variable.html',hobby=hobby,user=user,person=person)

# jinja2的判断器
@app.route('/if/<int:age>')
def if_demo(age):
    return render_template('if.html',age=age)

# jinja2的循环器
@app.route('/for')
def for_demo():
    users = [
        {'username':'tom','email':'tom@gmail.com'},
        {'username':'jerry','email':'jerry@gmail.com'},
        {'username':'kids0cn','email':'kids0cn@gmail.com'}
    ]
    return render_template('for.html',users=users)

# add_url_rule 的方式来注册路由
def addurl():
    return "add url rule"

app.add_url_rule('/addurl','addurl',addurl)


# 测试返回体
# 实际上每个仕途函数返回的是一个响应体，响应体包含响应状态码，响应头，响应体、
# 我们可以自己构造这个响应体

@app.route('/response')
# '''
#     默认是
#     状态码 200
#     文本类型 text/html
# '''
def response():
    # return 'response',200,{'Content-Type':'text/html'}
    headers = {
        'Content-Type':'text/plain', # 以文本方式解读代码
        'Server':'Flask',
        'location':'https://www.baidu.com'  # 重定向测试
    }

    response = make_response('<html></html>',301,headers)
    return response
