"""
@Project -> File   : flaskServer -> app.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/3/31 16:05
@Desc   :
"""
import os
from flask import Flask, render_template
from datetime import timedelta

# 创建Flask应用程序实例
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


# Flask中定义路由是通过装饰器实现的
@app.route('/')
def index_page():
    # return render_template("index.html")
    return render_template("功能验证版主页.html")


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
