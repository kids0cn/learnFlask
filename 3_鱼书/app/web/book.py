'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 17:13:43
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-11 17:53:40
FilePath: /learnFlask/3_鱼书/app/web/book.py
Description: 
    Blueprint 蓝图的作用是在大型项目中分拆模块的，而不是简单拆文件
Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook_old as YushuBook
from flask import jsonify
from flask import request as flask_request
from flask import current_app
from app.forms.book import SearchForm
#from app.view_models.book import BookViewModel,BookViewModel_collection
import json
from flask import render_template
from flask import flash
from . import web

@web.route('/book/search/<q>')
def search(q):
    # r = flask_request.args.to_dict()
    # current_app.logger.info('r: %s' % r)
    current_app.logger.info('搜索关键字：%s' % q)
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        current_app.logger.info('调用关键词搜索：搜索关键字：%s' % q)
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # 返回json数据,这个就相当于是一个api
    # return json.dumps(result),200,{'content-type':'application/json'}




@web.route('/book/seek')
def seek():
    """
    seek?q=地坛
    seek?q=9787501524044
    """

    # wtform验证层    
    form = SearchForm(flask_request.args)
    books = BookViewModel_collection()
    if form.validate():
        # 从form里取参数，可以使默认参数生效
        q = form.q.data.strip()
        current_app.logger.info('q: %s' % q)
        isbn_or_key = is_isbn_or_key(q)

        yushubook = YuShuBook()
        
        if isbn_or_key == 'isbn':
            yushubook.search_by_isbn(q)
        else:
            yushubook.search_by_keyword(q)
        books.fill(yushubook,q)
        # return jsonify(books.dict())   # 调用的事__dict__方法,会把对象所有的属性都返回,如果里面有一个object（列表）则还是不能返回，需要调用这个object的__dict__方法
        return json.dumps(books,default=lambda x:x.__dict__)
    else:
        return jsonify(form.errors)

# @web.route('/test')
# def hello_world():
#     current_app.logger.info("测试日志")
#     current_app.logger.warning("Warning msg")
#     current_app.logger.error("Error msg!!!")
#     return 'Hello, World!'

@web.route('/test')
def test():
    r = {
        'name':'kid',
        'age':18
    }
    r1 = [
        {'name':'kid1',
        'age':19},
        {'name':'kid2',
        'age':20},
        {'name':None,
        'age':None}
    ]


    flash('测试flash')

    # 调用模版
    return render_template('test.html',data=r,data1=r1)
