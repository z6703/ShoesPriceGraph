"""
@Project -> File   : flaskServer -> app.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/3/31 16:05
@Desc   :
"""
from datetime import timedelta

from flask import Flask, render_template, request, redirect
import re

import controller

# 创建Flask应用程序实例
app = Flask(__name__)
app_controller = controller.Controller()
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=360)
app.DEBUG = True
app.jinja_env.auto_reload = True


@app.before_request
def before_request():
    temp = str(request.path)[1:]
    if re.match(r"^(search_shoes|line_charts|search_colors|static)", temp) or not temp:
        return None
    else:
        print(str(request.path))
        return redirect("/")


# Flask中定义路由是通过装饰器实现的
@app.route('/')
def index_page():
    """
    主页
    :return: index.html
    """
    return render_template("index.html")


@app.route('/search_shoes', methods=['POST'])
def search_shoes():
    """
    使用名称搜索对应的鞋
    :return: 返回对应的鞋
    """
    name = request.form.get("name")
    res = app_controller.search_shoes(name)
    if not res:
        return render_template("index.html")
    else:
        return render_template("search_results.html", search_res=res)


@app.route('/search_colors/<shoes_id>', methods=['GET'])
def search_colors(shoes_id):
    """
    根据鞋的id搜索所有配色，返回一个二维列表包含配色名称、图片链接
    :param shoes_id:
    :return: [[color_name, img_link], [color_name, img_link]]
    """
    res = app_controller.search_specific_shoes(shoes_id)
    return render_template("choose_color.html", search_res=res, shoes_id=shoes_id)


@app.route('/search_graph/<shoes_id>/<color_id>', methods=['POST'])
def search_graph(shoes_id, color_id):
    size = request.form.get("options")
    show_img = app_controller.get_img(shoes_id, color_id, size)
    args = [shoes_id, color_id, size]
    return render_template("img_chart.html", show_img=show_img, args=args)


@app.route('/line_chart/<shoes_id>/<color_id>/<size>', methods=['GET'])
def draw_line_chart(shoes_id, color_id, size):
    line = app_controller.get_chart(shoes_id, color_id, size)
    return line.dump_options_with_quotes()


if __name__ == '__main__':
    app.run()
