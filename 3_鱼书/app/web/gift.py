'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 14:55:25
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-18 16:03:03
FilePath: /learnFlask/3_鱼书/app/web/gift.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from flask_login import login_required,current_user
from . import web
from app.models.gift import Gift
from app.models.base import db
from flask import current_app,flash
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from flask import redirect,url_for


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'my gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        # try:
        #     gift = Gift()
        #     gift.isbn = isbn
        #     gift.uid = current_user.id  # 当前登录用户,这是在user模型中定义的，交给login_manager管理
        #     gift.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
        #     db.session.add(gift)
        #     db.session.commit()
        # except Exception as e:
        #     db.session.rollback()  # 若插入出现错误回滚，安全
        #     raise ei
        with auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            gift.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)

    else:
        flash('这本书已添加到你的赠送清单或心愿清单')
    return redirect(url_for('web.book.book_detail',isbn=isbn))
    # 用重定向的技术，需要先返回给前端，前端在调用book_detail的视图函数，再返回给前端
    # 不仅需要刷新页面，也会增加服务器压力，用ajax可以在前端做处理，改善服性能
    # 也可以把这个页面缓存起来，直接返回也不用调用新的视图函数


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass



