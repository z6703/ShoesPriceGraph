"""
@Project -> File   : flaskServer -> app.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/3/31 16:05
@Desc   :
"""
import logging
import re
from datetime import timedelta
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request, redirect

import controller

# 创建Flask应用程序实例
app = Flask(__name__)
app_controller = controller.Controller()
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=360)
# 日志记录等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
file_log_handler = RotatingFileHandler("logs/flask.log", maxBytes=1024000, backupCount=10)
# 设置日志的格式   日志等级    文件名    函数名   行数   日志信息
formatter = logging.Formatter('%(levelname)s File = %(filename)s Function = %(funcName)s Line = %(lineno)d %(message)s')
# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)
black_list = set()


@app.before_request
def before_request():
    # print("\n\nBefore request")
    # print(time.asctime(time.localtime(time.time())))
    # print("source ip: " + str(request.remote_addr))
    # print("request path: " + str(request.path))
    # print("request.method: " + str(request.method))
    # print("---headers--start---")
    # print(str(request.headers).rstrip())
    # print("---headers--end----")
    # print("GET args: " + str(request.args))
    # print("POST args: " + str(request.form) + "\n\n")
    if request.remote_addr in black_list:
        print("current black list: ", black_list)
        return "有非法访问记录，IP已加入黑名单"
    if not (str(request.method) == "GET" or str(request.method) == "POST"):
        black_list.add(request.remote_addr)
        logging.critical("illegal request method, args = " + str(request.method))
        logging.critical("current black list " + str(black_list))
        return "有非法访问记录，IP已加入黑名单"
    temp = str(request.path)[1:]
    if re.match(r"^(search_shoes|line_chart|search_colors|search_graph|static)", temp) or not temp:
        return None
    else:
        black_list.add(request.remote_addr)
        logging.critical("illegal request path, args = " + str(request.path))
        logging.critical("current black list " + str(black_list))
        return "有非法访问记录，IP已加入黑名单"


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
    res = []
    try:
        res = app_controller.search_shoes(name)
    except Exception as e:
        logging.error("error occurred while searching shoes, args = " + name)
        logging.exception(e)
    if not res:
        return redirect("/")
    return render_template("search_results.html", search_res=res)


@app.route('/search_colors/<shoes_id>', methods=['GET'])
def search_colors(shoes_id):
    """
    根据鞋的id搜索所有配色，返回一个二维列表包含配色名称、图片链接
    :param shoes_id: 鞋的id
    :return: [[color_name, img_link], [color_name, img_link]]
    """
    res = []
    try:
        res = app_controller.search_specific_shoes(shoes_id)
    except Exception as e:
        logging.error("error occurred while searching colors, args = " + shoes_id)
        logging.exception(e)
    if not res:
        return redirect("/")
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
