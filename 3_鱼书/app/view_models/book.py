'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-08 21:55:17
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-08 22:10:21
FilePath: /learnFlask/3_鱼书/app/view_models/book.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''


class BookViewModel:
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
