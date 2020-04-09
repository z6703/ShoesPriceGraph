# -*- coding: UTF-8 -*-
"""
@Project -> File   : flaskServer -> controller.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/4/7 21:17
@Desc   : 业务逻辑
"""
import pickle

import shoes


class Controller:
    def __init__(self):
        pass

    def search_shoes(self):
        pass

    def search_specific_shoes(self, shoes_id: shoes):
        pkl_file = open('shoes.pkl', 'rb')
        obj = pickle.load(pkl_file)
        res = []
        for i in obj.color_info:
            res.append([i.color_name, i.img_link])
        return res

    def get_chart(self, shoes_id, color_id, size):
        date = ["2020/03/30", "2020/03/31", "2020/04/01", "2020/04/02", "2020/04/03", "2020/04/04", "2020/04/05",
                "2020/04/06", "2020/04/07", "2020/04/08", "2020/04/09", "2020/04/10"]
        price = [100, 200, 300, 500, 200, 300, 100, 200, 300, 500, 200, 300]

        return date, price
