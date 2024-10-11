'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-08 21:55:17
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-10 16:16:01
FilePath: /learnFlask/3_鱼书/app/view_models/book.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''


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
    def __init__(self,yushu_book):
            self.title = yushu_book.data['title'],
            self.publisher = yushu_book.data['publisher'],
            self.pages = yushu_book.data['pages'] or '',
            self.author = '、'.join(yushu_book.data['author']),
            self.price = yushu_book.data['price'] or '',
            self.summary = yushu_book.data['summary'] or '',
            self.image = yushu_book.data['image']
    


class BookViewModel_collection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,yushu_book):
        self.total = yushu_book.total
        self.keyword = yushu_book.keyword
        self.books = [BookViewModel_single(book) for book in yushu_book.books]

        