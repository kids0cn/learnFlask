'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 17:13:43
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-01 19:30:42
FilePath: /learnFlask/3_鱼书/app/web/book.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from flask import jsonify
from flask import Blueprint
from flask import current_app



web = Blueprint('web',__name__)

@web.route('/book/search/<q>/<page>')
def search(q,page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # 返回json数据,这个就相当于是一个api
    # return json.dumps(result),200,{'content-type':'application/json'}

# @web.route('/test')
# def hello_world():
#     current_app.logger.info("测试日志")
#     current_app.logger.warning("Warning msg")
#     current_app.logger.error("Error msg!!!")
#     return 'Hello, World!'