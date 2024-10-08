'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 17:13:43
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-08 22:08:28
FilePath: /learnFlask/3_鱼书/app/web/book.py
Description: 
    Blueprint 蓝图的作用是在大型项目中分拆模块的，而不是简单拆文件
Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import jsonify
from flask import request as flask_request
from flask import current_app
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel


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
    search?q=地坛
    search?q=9787501524044
    """

    # wtform验证层    
    form = SearchForm(flask_request.args)
    
    if form.validate():
        # 从form里取参数，可以使默认参数生效
        q = form.q.data.strip()
        current_app.logger.info('q: %s' % q)
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(q,result)
        else:
            result = YuShuBook.search_by_keyword(q)
            result = BookViewModel.package_collection(q,result)
        return jsonify(result)
    else:
        return jsonify(form.errors)

# @web.route('/test')
# def hello_world():
#     current_app.logger.info("测试日志")
#     current_app.logger.warning("Warning msg")
#     current_app.logger.error("Error msg!!!")
#     return 'Hello, World!'