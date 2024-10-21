'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-08 21:55:17
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-21 16:30:50
FilePath: /learnFlask/3_鱼书/app/view_models/book.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
from bs4 import BeautifulSoup
import requests
requests.packages.urllib3.disable_warnings()
import re
from app.spider.yushu_book import YuShuBook
import concurrent.futures
import json



proxy = {
    'http':'http://192.168.1.16:7893',
    'https':'http://192.168.1.16:7893',
}




class BookViewModel_single:
    '''
    # 重写本类，因为上面的类是面向过程的，只是封装了
    # 到了一个类里
    # 类最终的是：描述特征（类变量）和行为（方法），比如上面的类，就没有描述特征，
    即没有存储数据

    如何判断自己的类写的符不符合面向对象方法，
    看自己的方法是不是大量的使用了@classmethod和@staticmethod
    如果大量使用，说明这个类是面向过程的，不是面向对象的
    
    单本数据和集合数据分不开的时候，可以单独定一个单本的类
    单本的类就是处理单本书的裁切
    集合就是把多本书分别交给单本来处理

    '''
    def __init__(self,response,isbn):
        # with open('response.txt','a',encoding='utf-8') as f:
        #     f.write(str(response))
        #     f.write('++\n')
        if response:
            self.title = response.get('title','Null title')+':'+response.get('book_subtitle','')
            self.publisher = '、'.join(response['press'])
            self.pages = response['pages'][0] or ''
            self.author = '、'.join(response['author'])
            self.price = response['price'][0] or ''
            self.summary = response['intro']  or ''
            self.image = response['pic']['large']
            self.pubdate = response['pubdate'][0]
            self.isbn = isbn
            # with open('response.txt','a',encoding='utf-8') as f:
            #     f.write(str(self.title))
            #     f.write('\n')
            #     f.write(str(self.publisher))
            #     f.write('\n')
            #     f.write(str(self.pages))
            #     f.write('\n')
            #     f.write(str(self.author))
            #     f.write('\n')
            #     f.write(str(self.price))
            #     f.write('\n')
            #     f.write(str(self.summary))
            #     f.write('\n')
            #     f.write(str(self.image))
            #     f.write('\n')
        else:
            self.title = 'Null title'
    
    @property
    def intro(self):
        # 用来显示/作者/出版社/价格 ，如果有一个是空，就不显示，变成['作者'，'价格']
        intros = filter(lambda x:True if x else False,
                        [self.author,self.publisher,self.price])
        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(list(intros))
        # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return ' / '.join(intros)


class BookViewModel_collection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,yushu_book,session):
        self.total = yushu_book.total
        # print(yushu_book.keyword)
        self.keyword = yushu_book.keyword
        if self.total ==1 :            
            self.books.append(BookViewModel_single(yushu_book.books,yushu_book.isbn))
        else:
            self.__process_multibooks(yushu_book.books,session)

    def __process_multibooks(self,books,session):
        #print(books)
        url_list = []
        for item in books['items']:
            if item['type_name'] == '图书':
                uri_raw = item['target']['uri']
                #print(uri_raw)
                uri = re.findall(r'book/(\d+)',uri_raw)[0]
                url = f'https://book.douban.com/subject/{uri}/'
                #print(url)
                url_list.append(url)
        self.total = len(url_list)
        # print("++++++++++++++++url_list++++++++++++++++++++")
        # print(url_list)
        # print("++++++++++++++++url_list++++++++++++++++++++")
        self.__process_isbn_list(url_list,session)
                # isbn = self.__get_isbn(self.__get_http(url))
                # print(isbn)
                # if isbn:
                #     # yushubook = YuShuBook()
                #     #yushubook.search_by_isbn(isbn)
                #     self.books.append(BookViewModel_single(yushubook.books))
                #     self.total += 1




    def __process_isbn_list(self,url_list,session):
        # return books 列表直接把self.books填充
        with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
            # 使用session发送请求
            result = list(executor.map(lambda url: self.__get_book_detail(session,url),url_list))
            self.books = result


    def __get_isbn(self,response):
        if response.status_code == 200:
            source = response.content.decode('utf-8')
            soup = BeautifulSoup(source,'html.parser')
            # with open('antusheng.txt','w',encoding='utf-8') as f:
            #     f.write(soup.prettify())
            #查找isbn
            isbn_block = soup.find('script',type='application/ld+json').string
            # print("++++++++++++++++isbn_block++++++++++++++++++++")
            # print(isbn_block)
            #isbn = isbn_block.find('span',class_='pl',string='ISBN:').next_sibling.strip()
            isbn_json = json.loads(isbn_block)


            isbn = isbn_json.get('isbn','None')

            if isbn:
                #print(f'ISBN: {isbn}')
                return isbn

            else:
                print('未找到 ISBN')
                return 'None'
        
    def __get_http(self,session,url):
        headers = {
            'User-Agent':'Apifox/1.0.0 (https://apifox.com)',
        }
        r = session.get(url,headers=headers,verify=False)

        return r
    
    def __get_book_detail(self,session,url):
        # 输入：books的真实地址
        # 输出：self.book的内容
        isbn = self.__get_isbn(self.__get_http(session,url))
        if isbn:
            yushubook = YuShuBook()
            yushubook.search_by_isbn(isbn,session)
            return BookViewModel_single(yushubook.books)



class BookViewModel_old:
    # 不管是单本还是多本，都返回同样的数据类型
    def package_single(self,keyword,data):
        returned = {
            'keyword':keyword,
            'book':[],
            'total':0
        }
        if data:
            returned['total'] = 1
            returned['book'] = [self.cut_data(data)]
        return returned

    def package_collection(self,keyword,data):
        returned = {
            'keyword':keyword,
            'book':[],
            'total':0
        }
        if data:
            returned['total'] = len(data['books'])
            # 对单项数据进行处理，遇到多项的数据，就可以直接复用，这是一种编程思维
            returned['book'] = [self.cut_data(book) for book in data['books']]
        return returned
    
    def cut_data(self,data):
        # 这里需要重写和测试
        book =  {
            'title':data['title'],
            'publisher':data['publisher'],
            'pages':data['pages'] or '',
            'author': '、'.join(data['author']),
            'price':data['price'] or '',
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book