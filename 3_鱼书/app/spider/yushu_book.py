'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 16:53:12
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-12 15:41:09
FilePath: /learnFlask/3_鱼书/app/spider/yushu_book.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

from app.libs.myHttp import HTTP
from flask import current_app
import requests
class YuShuBook_old:
    # isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    douban_isbn_api = 'https://frodo.douban.com/api/v2/book/isbn/'
    douban_keyword_api = 'https://frodo.douban.com/api/v2/search/weixin'
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
        # current_app.logger.info(url)    
        result = HTTP.get(cls.douban_isbn_api+isbn,return_json=True,params=params,headers=headers)
        '''
        # 先从数据库查一下isbn，有的话直接返回
        # 没有的话，调用豆瓣api
        # 返回结果
        参考伪代码
        book = query_book_by_isbn(isbn)
        if book:
            return book
        else:
            result = HTTP.get(cls.douban_isbn_api+isbn,return_json=True,params=params,headers=headers)
            if result.get('status') == 'success':
                book = result.get('book')
                return book
            else:
                return None

        '''
        return result
    
    @classmethod
    def search_by_keyword(cls,q):
        current_app.logger.info('keyword搜索,keyword: %s' % q)
        headers = {
            'Referer':'https://servicewechat.com/wx2f9b06c1de1ccfca/95/page-frame.html',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.52(0x18003425) NetType/WIFI Language/zh_CN',
            'HOST':'frodo.douban.com' # HOST指定目标主机
        }
        params = {
            'q':q,
            'count':15,
            'start':0,
            'apiKey':cls.api_key,
        }
        
        result = HTTP.get(cls.douban_keyword_api,return_json=True,params=params,headers=headers)
        return result

class YuShuBook:
    # 这个类之所以是伪类是因为把所有的方法数据都返回给了别人，自己没有存储数据
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []
        self.session = requests.Session()

    # isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    # keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    douban_isbn_api = 'https://frodo.douban.com/api/v2/book/isbn/'
    douban_keyword_api = 'https://frodo.douban.com/api/v2/search/weixin'
    api_key = '0ac44ae016490db2204ce0a042db2916'

    
    def search_by_isbn(self ,isbn):
        headers = {
            'User-Agent':'MicroMessenger/',
            'Referer':'https://servicewechat.com/wx2f9b06c1de1ccfca/91/page-frame.html'
            }
        params = {
            'apiKey':self.api_key,
        }
        # current_app.logger.info(url)    
        result = HTTP.get(self.session,self.douban_isbn_api+isbn,return_json=True,params=params,headers=headers)
        '''
        # 先从数据库查一下isbn，有的话直接返回
        # 没有的话，调用豆瓣api
        # 返回结果
        参考伪代码
        book = query_book_by_isbn(isbn)
        if book:
            return book
        else:
            result = HTTP.get(cls.douban_isbn_api+isbn,return_json=True,params=params,headers=headers)
            if result.get('status') == 'success':
                book = result.get('book')
                return book
            else:
                return None

        '''

        self.__fill_single(result,isbn)
    
    
    def search_by_keyword(self,q):
        current_app.logger.info('keyword搜索,keyword: %s' % q)
        headers = {
            'Referer':'https://servicewechat.com/wx2f9b06c1de1ccfca/95/page-frame.html',
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.52(0x18003425) NetType/WIFI Language/zh_CN',
            'HOST':'frodo.douban.com' # HOST指定目标主机
        }
        params = {
            'q':q,
            'count':15,
            'start':0,
            'apiKey':self.api_key,
        }
        
        result = HTTP.get(self.session,self.douban_keyword_api,return_json=True,params=params,headers=headers)
        self.__fill_collection(result,q)
    
    def __fill_single(self,data,q):
        if data:
            self.total = 1
            self.books = data
            self.keyword = q

    def __fill_collection(self,data,q):
        if data:
            self.total = 0
            self.books = data
            self.keyword = q
