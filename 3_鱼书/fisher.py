'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 14:48:16
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-01 19:23:56
FilePath: /learnFlask/3_鱼书/fisher.py
Description: 
    视图函数不要写太多业务代码，特别的长，特别乱不易于维护
    启动文件也要干净，只做初始化等工作，视图函数放在app/web/book.py中

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''


from app import create_app


app = create_app()


if __name__ == '__main__':

    app.run(host='0.0.0.0')


