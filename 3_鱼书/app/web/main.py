'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-14 14:55:25
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-15 11:36:41
FilePath: /learnFlask/3_鱼书/app/web/main.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from . import web


__author__ = '七月'


@web.route('/')
def index():
    return 'index'


@web.route('/personal')
def personal_center():
    pass
