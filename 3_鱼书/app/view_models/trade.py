'''
Author: kids0cn kids0cn@gmail.com
Date: 2024-10-15 17:45:32
LastEditors: kids0cn kids0cn@gmail.com
LastEditTime: 2024-10-15 17:52:17
FilePath: /learnFlask/3_鱼书/app/view_models/trade.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''


class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self,goods):
        # 处理一组数据
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    # 处理单个对象
    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name = single.user.nickname,
            time = time,
            id = single.id
        )
