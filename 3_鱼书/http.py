'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 16:32:39
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-01 16:46:24
FilePath: /learnFlask/3_鱼书/http.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import requests



class HTTP:
    def get(self,url,return_json=True):

        # 通过判断状态码来判断是否成功得到返回的json
        # 代码大全建议说一个函数只有一个return，但是不同的return代表着不同的思维的分支，
        # 到了分支的终点就应该直接退出函数，
        # 如果强行使用一个return，可能会多出太多的if-else判断，导致代码复杂
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
