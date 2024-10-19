'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 14:55:25
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-18 16:02:46
FilePath: /learnFlask/3_鱼书/app/web/wish.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from . import web
from flask_login import login_required
from app.models.wish import Wish    
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.models.base import db
from flask import current_app, flash, redirect, url_for
from flask_login import current_user

@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        with auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已添加到你的赠送清单或心愿清单')
    return redirect(url_for('web.book.book_detail',isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
