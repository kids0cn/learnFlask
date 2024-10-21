'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 18:33:09
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-21 16:17:12
FilePath: /learnFlask/3_鱼书/app/__init__.py
Description: 
    初始化的工作应该放到__init__.py中，这样就可以在其他文件中导入app
    
__init__.py 文件通常用于以下几个目的：
1. 标识包：在 Python 中，包含 __init__.py 文件的目录被视为一个包。即使 __init__.py 文件是空的，它也能使目录成为一个包。
2. 初始化代码：__init__.py 文件可以包含包的初始化代码。当包被导入时，__init__.py 文件中的代码会自动执行。
3. 控制包的导入行为：可以在 __init__.py 文件中定义 __all__ 变量，来控制 from package import * 语句导入的内容。
4. 简化导入路径：通过在 __init__.py 文件中导入子模块，可以简化包的使用。
    例如，可以在 __init__.py 中导入 submodule，这样用户可以直接通过 import package 来使用 submodule。
Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from flask import Flask
from app.models.book import db # 要把db这个model跟这个app绑定
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


login_manager = LoginManager()
flask_bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    #app = Flask(__name__,template_folder='../templates',static_folder='../static')
    flask_bcrypt.init_app(app)
    app.config.from_object('app.config_secure')
    app.config.from_object('app.config_setting')
    register_blueprint(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login' # 告诉插件，哪个是登录页面
    login_manager.login_message = '请先登录'
    db.init_app(app) # 初始化db
    with app.app_context():
        db.create_all() # 创建数据表

    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)