'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-12 20:56:05
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-13 12:43:50
FilePath: /learnFlask/testConcurrent.py
Description: 
测试并发请求图书信息

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import concurrent.futures
import requests
import time

proxy = {
    'http':'http://192.168.1.16:7893',
    'https':'http://192.168.1.16:7893',
}

source = ['https://book.douban.com/subject/1084336/', 'https://book.douban.com/subject/3693974/', 'https://book.douban.com/subject/20443559/', 'https://book.douban.com/subject/26941417/', 'https://book.douban.com/subject/10572251/', 'https://book.douban.com/subject/4872917/', 'https://book.douban.com/subject/35695328/', 'https://book.douban.com/subject/30258611/', 'https://book.douban.com/subject/30203775/', 'https://book.douban.com/subject/26647054/', 'https://book.douban.com/subject/35291171/']
source1 = ['https://book.douban.com/subject/1084336/']
print(type(source))

def get_http(url):
    headers = {
        'User-Agent':'Apifox/1.0.0 (https://apifox.com)',
    }
    r = requests.get(url,headers=headers,proxies=proxy).content.decode('utf-8')

    print(r)
    return r


def get_book_info():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        resulut = list(executor.map(get_http,source))
    with open('result.txt','w',encoding='utf-8') as f:
        f.write(str(resulut))

start_time = time.time()
get_book_info()
end_time = time.time()
print(f'总耗时：{end_time - start_time}秒')


