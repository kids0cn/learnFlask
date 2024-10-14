'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-02 00:05:04
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-14 14:57:49
FilePath: /learnFlask/3_鱼书/app/web/__init__.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from flask import Blueprint

web = Blueprint('web',__name__)
#web = Blueprint('web',__name__,template_folder='../templates',static_folder='../static') #属于蓝图的static文件注册

from app.web import book
from app.web import wish
from app.web import gift
from app.web import drift
from app.web import main
from app.web import auth
