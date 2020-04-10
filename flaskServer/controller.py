# -*- coding: UTF-8 -*-
"""
@Project -> File   : flaskServer -> controller.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/4/7 21:17
@Desc   : 业务逻辑
"""
import pickle

from pyecharts import options as opts
from pyecharts.charts import Line

import shoes


class Controller:
    def __init__(self):
        pass

    def search_shoes(self, name):
        """
        实用名称模糊搜索，返回一个二维列表包含配色名称、图片链接和配色总数
        :return:[["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"]]
        """
        return [["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"]]

    def search_specific_shoes(self, shoes_id: shoes):
        """
        根据鞋的id搜索所有配色，返回一个三维列表包含配色名称、图片链接和有效的尺寸
        :param shoes_id:
        :return: [[color_name, img_link,[36,41,43]], [color_name, img_link, [41,42,43]]]
        """
        pkl_file = open('shoes.pkl', 'rb')
        obj = pickle.load(pkl_file)
        res = []
        for i in obj.color_info:
            res.append([i.color_name, i.img_link, [x for x in range(36, 49)]])
        return res

    def get_chart(self, shoes_id, color_id, size):
        date = ["2020/03/30", "2020/03/31", "2020/04/01", "2020/04/02", "2020/04/03", "2020/04/04", "2020/04/05",
                "2020/04/06", "2020/04/07", "2020/04/08", "2020/04/09", "2020/04/10"]
        price = [100, 200, 300, 500, 200, 300, 100, 200, 300, 500, 200, 300]
        line = self.line_base(date, price)
        return line

    def line_base(self, date: list, price: list) -> Line:
        line = (
            Line()
                .add_xaxis(xaxis_data=date)
                .add_yaxis(
                series_name="价格",
                y_axis=price,
                markpoint_opts=opts.MarkPointOpts(
                    data=[
                        opts.MarkPointItem(type_="max", name="最大值"),
                        opts.MarkPointItem(type_="min", name="最小值"),
                    ]
                ),
                markline_opts=opts.MarkLineOpts(
                    data=[opts.MarkLineItem(type_="average", name="平均值")]
                ),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="历史价格记录"),
                tooltip_opts=opts.TooltipOpts(trigger="axis"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
            )
        )
        return line

    def run_crawler(self):
        while True:
            pass
