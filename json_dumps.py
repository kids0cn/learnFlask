'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-11 19:23:06
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-12 14:59:46
FilePath: /learnFlask/json_dumps.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

import json
import re
import requests
from time import sleep
from bs4 import BeautifulSoup


def read_json(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return json.load(f)
    
def produce_single(response):
    data = {
        'title':response['title']+response['book_subtitle'] or '',
        'publisher' : '、'.join(response['press']),
        'pages' : response['pages'] or '',
        'author' : '、'.join(response['author']),
        'price' : response['price'] or '',
        'summary' : response['intro'].replace('\n','') or '',
        'image' : response['pic']['normal']
    }
    return data


def produce_collection(response):
    pass
    

douban_isbn_api = 'https://frodo.douban.com/api/v2/book/isbn/'
douban_keyword_api = 'https://frodo.douban.com/api/v2/search/weixin'
api_key = '0ac44ae016490db2204ce0a042db2916'




def get_isbn(url):


    # 发起 GET 请求
    response = get_http(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 HTML 内容
        source = response.content.decode('utf-8')

        soup = BeautifulSoup(source, 'html.parser')

        # 查找 ISBN
        isbn_element_block = soup.find('div',id='info')
        isbn = isbn_element_block.find('span',class_='pl',string='ISBN:').next_sibling.strip()
        if isbn:
            print(f'ISBN: {isbn}')
            return isbn
        else:
            print('未找到 ISBN')
            return 'None'
    else:
        print(f'请求失败，状态码: {response.status_code}')


def get_http(url):
    headers = {
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
} 
    r = requests.get(url,headers=headers,verify=False)
    return r

if __name__ == '__main__':
    # response = read_json('multi_response.json')
    # for item in response['items']:
    #     if item['type_name'] == '图书':
    #         uri_raw = item['target']['uri']
    #         print(uri_raw)
    #         uri = re.findall(r'book/(\d+)',uri_raw)[0]
    #         url = f'https://book.douban.com/subject/{uri}/'
    #         isbn = get_isbn(url)
    #         print(isbn)
    #         '''
    #         找到isbn后，调用isbn search函数，获取单本图书信息
    #         把图书信息加入[]
            
    #         '''
    #         break
    URL = 'https://book.douban.com/subject/35520785/'
    isbn = get_isbn(URL)
    print(isbn)




