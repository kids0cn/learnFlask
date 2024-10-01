'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 14:48:16
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-01 16:29:52
FilePath: /learnFlask/3_鱼书/fisher.py
Description: 
    视图函数不要写太多业务代码，特别的长，特别乱不易于维护

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask import Flask,render_template
from helper import is_isbn_or_key

app = Flask(__name__)


@app.route('/book/search/<q>/<page>')
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    pass



