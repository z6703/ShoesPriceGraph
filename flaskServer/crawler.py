# -*- encoding: utf-8 -*-
'''
@File    :   crawler.py    
@Contact :   1044977628@qq.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/1/10 19:58   zwf      1.0         None
'''

import math
import re
from concurrent.futures.thread import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup

import shoes
from mysql_operator import MysqlOperator as SQL

# import _thread


'''
识货首页：crawl_all_shihuo
    分类：crawl_single_shihuo
        篮球
        跑鞋
        休闲鞋
            名称，图片链接，尺寸，价格
'''


class Crawler:
    def __init__(self, url):
        self.url = url
        self.header = {
            'Cookie': 'cnzz_CV30020080=buzi_cookie%7Cb3ff8c35.9d4a.493a.d8dc.bf7f43622e9e%7C-1; _shcid=FaGfDZblNSRtxsgVn98Q; UM_distinctid=16f7a85e4a470c-034b9e9879e064-6701b35-144000-16f7a85e4a539e; __gads=ID=a153c6271a9dfc74:T=1578308615:S=ALNI_MaloO7v068TIwt7y_TyLucmi3OScA; _dacevid3=b3ff8c35.9d4a.493a.d8dc.bf7f43622e9e; _cnzz_CV30020080=buzi_cookie%7Cb3ff8c35.9d4a.493a.d8dc.bf7f43622e9e%7C-1; _HUPUSSOID=9f9205b0-d94d-4740-9c68-51a2c86ff206; history=be1fRzXIcereUry4UIB1ZALO0U0GcsVfMkCuKZOKhnF55dD1zyI59GhnI%2FZTUUPvM3II4r5cFy9ys8FdKYdSOLXfMne7fhGVdFzQOzcy4TDXMbxCfDq8Lg0t3UM4pmtP3wv4jRKZEWG1YsfQ422ZTGWZ%2F04kVzbpL6UPddDZ5LDaXCH4GSV%2BEw8JshLlsG3Dxm64WbwowzLG29bhDk39PCXnkYW7SKlPVmz5HxatlKUqgnyi0jeKg1FLm%2FIVpvtvhVo9QiZxiEb9dlCX56BtQ8JQWlpl3oF5vAAfuB7nESvUBaTFWyyeAo33%2FzVwf0g57hPc1Ft3n9lDYPo085vOwO%2FWInVVkw53DeZckA6Kh%2FIPuvGqnOOT%2BAjDUcCgjod8ORgP8fK3I7VLsX1kIzy4%2Fgrbik23h83HAE7K2fEIjI7%2Bv%2F9CmM8s9PlNY2kTij8s23ezzNu%2BtEhEYVyozBYX0ub1638UVAoNc0UBApCOY2uIfTkBN1Rzg2LBwqbDXC92GJa35SjMHQLdX%2BOXJUgoLrvhzqMMP81BmmlebaeSFnjob9Op156Vmph4AXhhwuVIP6eOrjUkwEWYlG6cxuDZvYw5O3c4QS1vBHrktzKa%2BMiT9U05AM6eDclY49u5frbeLSJiuhxZd1DjbBaE11iPFYctAZtu4R3BKOJFIhOGc2tZc6S%2BNjlVhK0jSlZ89qk2EQf%2Bx%2BWkOxZ1nIb0SVhMUz0yAzu2hiYY7Q%2FRg4rx09TxBmn1N6CPnOFkLj%2F%2B7RsEL5s1b0%2FQNF5rZvbOV9Tp37IkVZzs6eeAi%2BCDx1twrGGN54ZB2tZ%2BgiRmoW4EEV%2Fq8vic9%2FYOk2MxPbHk5ewlKrMlMXg8F2h1e6ngqw; CNZZDATA30089914=cnzz_eid%3D106436118-1578304538-null%26ntime%3D1578659019; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f7a85e480385-052876ce6ba6fa-6701b35-1327104-16f7a85e48130e%22%2C%22%24device_id%22%3A%2216f7a85e480385-052876ce6ba6fa-6701b35-1327104-16f7a85e48130e%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; amvid=416c6298fe7fe7c74f1eaef6371dfd01; __dacevst=77f8cbec.f208b86e|1578665268300',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
        self.kinds = ['basketball',
                      'running',
                      'freestyle']
        self.all_size = [
            '35.5', '36', '36.5', '37.5', '38', '38.5',
            '39', '40', '40.5', '41', '42', '43', '43.5', '44', '44.5',
            '46', '47', '47.5', '48',
        ]
        self.sql = SQL()

    def show_url(self):
        print(self.url)

    def set_url(self, url):
        self.url = url

    # 识货有很多类别，每个类别单独爬，目前只爬鞋
    def crawl_all_shihuo(self, url=''):
        if len(url) > 0:
            self.url = url

        for kind in self.kinds:
            self.crawl_single_kind(kind)

    # 爬某个类别，找到所有下级链接
    def crawl_single_kind(self, kind='basketball'):
        print("GET: KIND = ", kind)
        # 爬取页面，找到页面中各个鞋的类别的页面
        url = 'http://www.shihuo.cn/' + kind + '/list?page_size=60&page=1'
        response = requests.get(url, headers=self.header)
        html = response.text

        # 首先找到总页面数
        start = html.find('var totalPage = parseInt(') + len('var totalPage = parseInt(')
        end = html.find(')', start)
        page_nums = math.ceil(float(html[start:end]))
        # print(page_nums)

        # 循环找到全部下级链接
        links = []
        for page_num in range(page_nums):
            url = 'http://www.shihuo.cn/' + kind + '/list?page_size=60&page=' + str(page_num)
            response = requests.get(url, headers=self.header)
            html = response.text
            soup = BeautifulSoup(html, "lxml")
            # print(soup.prettify())
            link_class = soup.select('#js_hover li .imgs-area .link ')
            for item in link_class:
                links.append('http:' + item['href'])

        thread_pool = ThreadPoolExecutor(8)
        for link in links:
            thread_pool.submit(self.crawl_all_color_for_shoes, link)
        thread_pool.shutdown(wait=True)
        # pool = Pool(8)
        # for link in links:
        #     pool.apply_async(self.crawl_all_color_for_shoes,link)
        # pool.close()
        # pool.join()

    # 爬某个鞋，不同配色，不同尺寸的最低价
    def crawl_all_color_for_shoes(self, url):
        print("GET: ", url)
        # print(datetime.datetime.now())

        shoes_info = shoes.Shoes()
         
        response = requests.get(url)  # , headers=self.header)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        # print(soup.prettify())
        # *******找到id,名字
        shoes_info.id = int(url.split('/')[-1].split('.')[0])
        shoes_info.name = soup.select('.scroll-wrap h2')[0].contents[0].split('\n')[1]

        # color_nums = soup.select('.proMore_block  ul li .all_color')[0].text[3:][:-3]

        # 找到所有配色id
        color_ids, pic_links, color_names = self.find_id_name_pic(html)

        for i, style_id in enumerate(color_ids):
            color_info = shoes.ColorInfo()
            color_info.color_id = int(style_id)
            color_info.img_link = pic_links[i]
            color_info.color_name = color_names[i]

            price_dict = dict()
            for size in self.all_size:
                data_url = 'http://www.shihuo.cn/sports/getSuppliers?goods_id=' + str(
                    shoes_info.id) + '&size=' + size + '&style_id=' + style_id + '&color=&supplier_id=&price_sort=asc&tag=&page=1&page_size=1'
                data = requests.get(data_url, headers=self.header).json()
                if data['count'] == 0:
                    price_dict[size] = 0
                else:
                    price_dict[size] = int(data['info'][0]['priceAll'][size])
            color_info.price_dict = price_dict

            shoes_info.append_color(color_info)

        self.sql.insert_shoes_data(shoes_info)

        print("SAVED: ", shoes_info.id)

        # print(datetime.datetime.now())
        # return shoes_info

    def demo_crawl(self, url):
        if len(url) > 0:
            self.url = url
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        response = requests.get(self.url, headers=headers)
        # data = response.json()
        result = []
        print(response.text)

    def find_id_name_pic(self, html):
        start = html.find('goods_styles = ')
        end = html.find('goods_tags = ', start)
        str = html[start:end].replace('\\x22', '')

        pattern = re.compile('id:\d+,')
        color_ids = pattern.findall(str)
        for i, _ in enumerate(color_ids):
            color_ids[i] = color_ids[i][3:][:-1]

        str = str.replace('\\\\\\', '')
        pattern = re.compile('pic:.*?,')
        pic_links = pattern.findall(str)
        for i, _ in enumerate(pic_links):
            pic_links[i] = 'http:' + pic_links[i][4:][:-1]

        str = str.replace('\\\\', '\\')
        str = str.replace('\\n', '').encode().decode('unicode-escape')

        pattern = re.compile(',name:.*?,')
        names = pattern.findall(str)
        for i, _ in enumerate(names):
            names[i] = names[i][6:][:-1]

        pattern = re.compile('_name:.*?,')
        official_names = pattern.findall(str)
        for i, _ in enumerate(official_names):
            names[i] += ',' + official_names[i][6:][:-1]

        return color_ids, pic_links, names


if __name__ == '__main__':
    url = 'http://www.shihuo.cn/sports/detail/424041.html#qk=list'
    crawler = Crawler(url=url)
    # si = crawler.crawl_all_color_for_shoes(url)
    # print(si.id)
    crawler.crawl_single_kind()
    # print(si)

    # pkl_file = open('shoes.pkl', 'wb')
    # pickle.dump(si,pkl_file)

    # sprint('over!')
