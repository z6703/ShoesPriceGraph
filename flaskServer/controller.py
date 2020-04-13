# -*- coding: UTF-8 -*-
"""
@Project -> File   : flaskServer -> controller.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/4/7 21:17
@Desc   : 业务逻辑
"""

from pyecharts import options as opts
from pyecharts.charts import Line

import mysql_operator as mo


class Controller:
    def __init__(self):
        self.op = mo.MysqlOperator()

    def search_shoes(self, name: str):
        """
        实用名称模糊搜索，返回一个二维列表包含匹配到的shoes_id、具体名称、随机配色的一张图片链接和配色总数
        :return:[["shoes_id","shoes_name", "img_link", "quantity"], ["shoes_id","shoes_name", "img_link", "quantity"]]
        """
        if not name:
            return
        res = self.op.search_by_name(name)
        print(res)
        return res

    def search_specific_shoes(self, shoes_id: int):
        """
        根据鞋的id搜索所有配色，返回一个三维列表包含配色名称、图片链接
        :param: shoes_id:
        :return: [[color_name, img_link, color_id, [valid_size]], [color_name, img_link, color_id, [valid_size]]]
        """
        res = self.op.search_color_id(shoes_id)
        for i, x in enumerate(res):
            res[i].append(self.get_valid_size(shoes_id, x[2]))
        return res

    def get_valid_size(self, shoes_id: int, color_id: int):
        """
        根据鞋的id和配色id搜索所有存在记录的尺寸，返回一个列表包含有效的尺寸
        :param: shoes_id, color_id
        :return: [36, 38, 41, 43]
        """
        res = self.op.search_size_list(shoes_id, color_id)
        return res

    def get_img(self, shoes_id, color_id, size):
        res = self.op.search_price_data(shoes_id, color_id, size)
        return res['img_link']


    def get_chart(self, shoes_id, color_id, size):
        """
        根据鞋的id、配色id、尺寸搜索记录，返回鞋名、配色名、价格、日期、图片链接
        :param shoes_id, color_id
        :return: [[shoes_name, color_name, img_link, ["2020/03/30", "2020/03/31", "2020/04/01"], [100, 200, 300]], [shoes_name, color_name, img_link, ["2020/03/30", "2020/03/31", "2020/04/01"], [100, 200, 300]]]
        """
        res = self.op.search_price_data(shoes_id, color_id, size)
        date = res["date_list"]
        price = res["price_list"]
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

if __name__ == '__main__':
    c = Controller()
    c.search_shoes("nik")
