'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 17:13:43
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-15 17:56:43
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
from app.view_models.book import BookViewModel_single,BookViewModel_collection
import json
from flask import render_template
from flask import flash
from . import web
import requests
# @web.route('/book/search/<q>')
# def search(q):
#     # r = flask_request.args.to_dict()
#     # current_app.logger.info('r: %s' % r)
#     current_app.logger.info('搜索关键字：%s' % q)
#     isbn_or_key = is_isbn_or_key(q)

#     if isbn_or_key == 'isbn':
#         result = YuShuBook.search_by_isbn(q)
#     else:
#         current_app.logger.info('调用关键词搜索：搜索关键字：%s' % q)
#         result = YuShuBook.search_by_keyword(q)
#     return jsonify(result)
#     # 返回json数据,这个就相当于是一个api
#     # return json.dumps(result),200,{'content-type':'application/json'}




@web.route('/book/search')
def search():
    """
    search?q=地坛
    search?q=9787501524044
    """

    # wtform验证层    
    form = SearchForm(flask_request.args)
    books = BookViewModel_collection()
    if form.validate():
        # 从form里取参数，可以使默认参数生效
        q = form.q.data.strip() #获取搜索关键字
        current_app.logger.info('q: %s' % q)
        isbn_or_key = is_isbn_or_key(q)
        with requests.session() as session: # 创建session对象
            yushubook = YuShuBook()
            if isbn_or_key == 'isbn':
                yushubook.search_by_isbn(q,session)
            else:
                yushubook.search_by_keyword(q,session)
            books.fill(yushubook,session)
            # return jsonify(books.dict())   # 调用的事__dict__方法,会把对象所有的属性都返回,如果里面有一个object（列表）则还是不能返回，需要调用这个object的__dict__方法
            #return json.dumps(books,default=lambda x:x.__dict__,ensure_ascii=False) # ensure_ascii=False 参数，以确保中文字符不会被转义为 Unicode 编码。这样可以保留中文字符的原始形式。

    else:
        flash("搜索的关键词不符合要求，请重新输入",category = 'error')
    return  render_template('search_result.html',books=books)



@web.route('/book/<isbn>/detail')
def book_detail(isbn):


    has_in_gifts = False
    has_in_wishes = False

    # TODO：封装youshubook,BOOKVIEWMODEL添加self.isbn，否则前端调用不到isbn
    with requests.session() as session:
        yushubook = YuShuBook()
        yushubook.search_by_isbn(isbn,session)
        book = BookViewModel_single(yushubook.book)
        return render_template('book_detail.html',book=book)
    
        if current_user.is_authenticated:
            if Gift.query.filter_by(isbn=isbn,uid=current_user.id,launched=False).first():
                has_in_gifts = True
            if Wish.query.filter_by(isbn=isbn,uid=current_user.id,launched=False).first():
                has_in_wishes = True

        # 显示所有赠送者的信息都查出来
        trade_gifts = Gift.query.filter_by(isbn=isbn,launched=False).all()
        # 显示所有心愿者的信息都查出来
        trade_wishes = Wish.query.filter_by(isbn=isbn,launched=False).all()

        trade_gifts_model = TradeInfo(trade_gifts)  
        trade_wishes_model = TradeInfo(trade_wishes)

        return render_template('book_detail.html',book=book,trade_gifts=trade_gifts_model,trade_wishes=trade_wishes_model,has_in_gifts=has_in_gifts,has_in_wishes=has_in_wishes)


# @web.route('/test')
# def hello_world():
#     current_app.logger.info("测试日志")
#     current_app.logger.warning("Warning msg")
#     current_app.logger.error("Error msg!!!")
#     return 'Hello, World!'

# @web.route('/test')
# 测试flash和模版渲染
# def test():
#     r = {
#         'name':'kid',
#         'age':18
#     }
#     r1 = [
#         {'name':'kid1',
#         'age':19},
#         {'name':'kid2',
#         'age':20},
#         {'name':None,
#         'age':None}
#     ]


#     flash('测试flash')

#     # 调用模版
#     return render_template('test.html',data=r,data1=r1)

