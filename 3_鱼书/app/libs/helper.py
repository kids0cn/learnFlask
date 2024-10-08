'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-01 15:09:17
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-01 16:16:34
FilePath: /learnFlask/3_鱼书/helper.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
def is_isbn_or_key(word):
    isbn_or_key = 'key'
    #  isbn 
    #      - 13 位  0-9数字
    #      - 10 位数字 里面含有 '-'
    if '-' in word:
        word_short = word.replace('-','')
        if (word_short.isdigit) and len(word_short==10):
            isbn_or_key = 'isbn'
    elif  word.isdigit and len(word) == 13:
        isbn_or_key = 'isbn'
    
    return isbn_or_key
    