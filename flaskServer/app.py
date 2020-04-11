"""
@Project -> File   : flaskServer -> app.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/3/31 16:05
@Desc   :
"""
from datetime import timedelta

from flask import Flask, render_template, request

import controller

# 创建Flask应用程序实例
app = Flask(__name__)
app_controller = controller.Controller()
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=360)
app.DEBUG = True
app.jinja_env.auto_reload = True


# Flask中定义路由是通过装饰器实现的
@app.route('/')
def index_page():
    """
    主页
    :return: index.html
    """
    # return render_template("index.html")
    return render_template("index.html")


@app.route('/search_graph', methods=['POST'])
def search_graph():
    """
    使用id搜索对应的图片
    返回对应的图片和价格折线图
    """
    size = request.form.get("options")
    print(size)
    res = "http://shihuo.hupucdn.com/def/20191028/bfb8c375e06ac175b91b004655fe73221572249491.jpg"
    return render_template("img_chart.html", show_img=res, chart_id=1)


@app.route('/line_chart/<chart_id>', methods=['GET'])
def draw_line_chart(chart_id):
    line = app_controller.get_chart(shoes_id=1, color_id=1, size=1)
    return line.dump_options_with_quotes()


@app.route('/search_colors/<shoes_id>', methods=['GET'])
def search_colors(shoes_id):
    """
    根据鞋的id搜索所有配色，返回一个二维列表包含配色名称、图片链接
    :param shoes_id:
    :return: [[color_name, img_link], [color_name, img_link]]
    """
    res = app_controller.search_specific_shoes(shoes_id)
    return render_template("choose_color.html", search_res=res)


@app.route('/search_shoes', methods=['POST'])
def search_shoes():
    """
    使用名称搜索对应的鞋
    :return: 返回对应的鞋
    """
    name = request.form.get("name")
    res = app_controller.search_shoes(name)
    return render_template("search_results.html", search_res=res)


# @app.route('/<int:id>/mainpage', methods=('GET', 'POST'))
# def mainpage(id):
#     root_dir = os.path.abspath(os.path.dirname(__file__))
#     img_path = root_dir + '\static' + '\images'  # 图片文件存储在static文件夹下的images文件夹内
#     files = os.listdir(img_path)  # 获取图片文件名字
#     if id == len(files):
#         id = 0
#     file = "/static/images/" + files[id]
#     return file


if __name__ == '__main__':
    app.run()
