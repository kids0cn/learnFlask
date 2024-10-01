'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-09-30 01:29:28
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-09-30 17:30:00
FilePath: /learnFlask/app.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

# 添加动态路由
@app.route('/usr/<name>')
def user(name):
    return '<h1>Hello,{}!</h1>'.format(name)

