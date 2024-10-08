'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-02 00:27:59
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-02 17:35:43
FilePath: /learnFlask/3_鱼书/app/forms/book.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from wtforms import Form,StringField
from wtforms.validators import Length  # 添加这行以导入Length

class SearchForm(Form):
    # 要学习这些成熟的模块，写这些短小可靠的函数，因为函数越简单，复用性越高
    q = StringField(validators=[Length(min=1,max=30)]) # q的长度必须在1-30之间
    # page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)