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
        实用名称模糊搜索，返回一个二维列表包含匹配到的具体名称、随机配色的一张图片链接和配色总数
        :return:[["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"]]
        """
        return [["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"], ["shoes_name", "img_link", "quantity"]]

    def search_specific_shoes(self, shoes_id: shoes):
        """
        根据鞋的id搜索所有配色，返回一个三维列表包含配色名称、图片链接
        :param shoes_id:
        :return: [[color_name, img_link], [color_name, img_link]]
        """
        # pkl_file = open('shoes.pkl', 'rb')
        # obj = pickle.load(pkl_file)
        # res = []
        # for i in obj.color_info:
        #     res.append([i.color_name, i.img_link, [x for x in range(36, 49)]])
        res = [['首发,Black/White', 'http://shihuo.hupucdn.com/def/20191028/bfb8c375e06ac175b91b004655fe73221572249491.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['黑红/禁穿,Bred', 'http://shihuo.hupucdn.com/def/20191220/bad112c092f4b2cfb99707cd2c26c8ff1576823015.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['新年/2020,CNY', 'http://shihuo.hupucdn.com/def/20200219/6f04ca223a0333f73675e16bf55a902e1582083971.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['紫罗兰,Grand Purple', 'http://shihuo.hupucdn.com/def/20191125/6724d2966c1987c197913022649fe6d41574686505.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['蓝色/黄色,Oracle Aqua', 'http://shihuo.hupucdn.com/trade/reposition/2020-02-01/aeb212ac64fdac0ad1772aa814519712.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['红色/金属金,Trophies', 'http://shihuo.hupucdn.com/trade/reposition/2020-01-23/b1d32c7a8c50b4bee53b05bcecb05b69.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['白黑,Oreo', 'http://shihuo.hupucdn.com/trade/reposition/2020-02-24/4c09e28510275d24ad50cb7754b0e539.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['Concepts联名/圣甲虫,Khepri', 'http://shihuo.hupucdn.com/def/20200219/b191dce2a537cb19af911f4659ed1ef91582083878.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['灰粉蓝,Vast Grey/Blue/Pink', 'http://shihuo.hupucdn.com/trade/reposition/2019-12-28/b1bb1b69af5d66f29bfec1f0bc794b77.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['中国新年/黄色,CNY', 'http://shihuo.hupucdn.com/trade/reposition/2019-12-29/91f6f385e95d9775f93fe986caf655bf.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['治愈世界,Preheat Collection/Heal  The World', 'http://shihuo.hupucdn.com/def/20191111/c7db467bee1eca53dad8741413c70f2c1573455552.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['黑色/炫银,Black/Silver', 'http://shihuo.hupucdn.com/def/20200405/206421a9b73373780013272c2a77fd621586072959.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['上海城市限定,Preheat Collection/Shanghai', 'http://shihuo.hupucdn.com/def/20191111/df083cb67432eb5a5fe92151ab2d5c2a1573456147.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['GS/紫罗兰,Enlightenment', 'http://shihuo.hupucdn.com/kupload2018/202035/15833783190000.webp', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['北京城市限定,Preheat Collection/Beijing', 'http://shihuo.hupucdn.com/def/20191111/c4ddd6e71645692e03ab6929a57c69c71573456128.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['广州城市限定,Preheat Collection/Guanzhou', 'http://shihuo.hupucdn.com/def/20191111/1bc0637bb9c66b44c04d99704fcaf4201573459314.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['白灰绿,There Is No Coming Back', 'http://shihuo.hupucdn.com/def/20200318/89017250e8f6893ef8355685e1877bcf1584522348.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['Concepts联名/木乃伊,Golden Mummy', 'http://shihuo.hupucdn.com/trade/reposition/2019-12-25/09c07b1cab351d7042a8d40cd77fcf73.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['台北城市限定,Preheat Collection/Taipei', 'http://shihuo.hupucdn.com/def/20191111/609f282ed587928c9462986973cb6cc81573456163.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['白色/蓝色,White Sapphire', 'http://shihuo.hupucdn.com/trade/reposition/2020-02-27/379652cdc2889cb2d1b6cbcb0bd28e83.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['洛杉矶城市限定,Preheat Collection/LA', 'http://shihuo.hupucdn.com/def/20191111/9384f2336a65d426e601231fdccea63a1573457465.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['东京城市限定,Preheat Collection/Tokyo', 'http://shihuo.hupucdn.com/def/20191110/891bbdbcd571bf77d10fba3c409574a41573375317.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['马尼拉城市限定,Preheat Collection/Manila', 'http://shihuo.hupucdn.com/def/20191111/8791573c4a6f9e0c64f0d05e4f92c8e41573460467.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['柏林城市限定,Preheat Collection/Berliin', 'http://shihuo.hupucdn.com/def/20191111/4f8b44ecf04da96197180c4ddf96d7121573461100.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['纽约城市限定,Preheat Collection/NYC', 'http://shihuo.hupucdn.com/def/20191111/6e7e706588c2de8fce3e2f743ed1c0a91573455375.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['休斯顿城市限定,Preheat Collection/Houston', 'http://shihuo.hupucdn.com/def/20191111/5792071c3e72ac902f96f51f88b434541573457349.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['迈阿密城市限定,Preheat Collection/Miami', 'http://shihuo.hupucdn.com/def/20191111/37656c7d82f1f1134a4268fd614b06e31573455801.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['黑色/大理石,null', 'http://shihuoproxy.hupucdn.com/aHR0cDovL2ltZy5hbGljZG4uY29tL2ltZ2V4dHJhL2kyLzM2MTI3MTkwMzkvTzFDTjAxRDBKSWNNMkdkdWJoN1UzRU9fISEzNjEyNzE5MDM5LmpwZw..', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['邀请赛/亲友限定,Invitational (F&F)', 'http://shihuo.hupucdn.com/def/20200203/81e5aae7a43dcc37ff5b93cd0d9c4a861580726280.jpg', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['红黑,Bruce Lee', 'http://shihuo.hupucdn.com/trade/reposition/2020-04-08/3bc7ebac7e53749d666fe748d0d69c3d.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]], ['白黑/黄红,Bruce Lee', 'http://shihuo.hupucdn.com/trade/reposition/2020-04-02/3fc396d7cdd8dbedcbd8a069b5ac2040.png', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]]]

        return res

    def get_valid_size(self, shoes_id, color_id):
        """
        根据鞋的id和配色id搜索所有存在记录的尺寸，返回一个列表包含有效的尺寸
        :param shoes_id, color_id
        :return: [36, 38, 41, 43]
        """
        valid_size = [36, 38, 41, 43]
        return valid_size

    def get_chart(self, shoes_id, color_id, size):
        """
        根据鞋的id、配色id、尺寸搜索记录，返回鞋名、配色名、价格、日期、图片链接
        :param shoes_id, color_id
        :return: [[shoes_name, color_name, img_link, ["2020/03/30", "2020/03/31", "2020/04/01"], [100, 200, 300]], [shoes_name, color_name, img_link, ["2020/03/30", "2020/03/31", "2020/04/01"], [100, 200, 300]]]
        """
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
