'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 16:53:12
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-01 20:34:47
FilePath: /learnFlask/3_鱼书/yushu_book.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from myHttp import HTTP
from flask import current_app

class YuShuBook:
    # isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    douban_book_api = 'https://frodo.douban.com/api/v2/book/isbn/'
    api_key = '0ac44ae016490db2204ce0a042db2916'
   # https://frodo.douban.com/api/v2/book/isbn/9787532796397?apiKey=0ac44ae016490db2204ce0a042db2916
   # 

    @classmethod
    def search_by_isbn(cls,isbn):
        headers = {
            'User-Agent':'MicroMessenger/',
            'Referer':'https://servicewechat.com/wx2f9b06c1de1ccfca/91/page-frame.html'
            }
        params = {
            'apiKey':cls.api_key,
        }
        url = cls.douban_book_api + isbn
        current_app.logger.info(url)    
        result = HTTP.get(url,return_json=True,params=params,headers=headers)
        return result
    def search_by_keyword(cls,keyword,count=15,start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result

    