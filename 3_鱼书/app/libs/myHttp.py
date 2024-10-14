'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 16:32:39
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-14 10:26:36
FilePath: /learnFlask/3_鱼书/app/libs/myHttp.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import requests
from flask import current_app
requests.packages.urllib3.disable_warnings()

proxy = {
    'http':'http://192.168.1.16:7890',
    'https':'http://192.168.1.16:7893',
}


class HTTP:
    @staticmethod # 静态方法，不需要实例化，可以直接调用,这个类可以不用的，封装到类里面，是为了方便以后扩展
    def get(url,session,return_json=True,params=None,headers=None):

        # 通过判断状态码来判断是否成功得到返回的json
        # 代码大全建议说一个函数只有一个return，但是不同的return代表着不同的思维的分支，
        # 到了分支的终点就应该直接退出函数，
        # 如果强行使用一个return，可能会多出太多的if-else判断，导致代码复杂    
        r = session.get(url,headers=headers,params=params,verify=False)
        if r.status_code != 200:
            #return {'豆瓣接口 status_code': r.status_code} if return_json else f'Status Code: {r.status_code}'
            return None
        return r.json() if return_json else r.text
