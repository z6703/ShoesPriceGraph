"""
@Project -> File   : flaskServer -> app.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/3/31 16:05
@Desc   :
"""
from datetime import timedelta

from flask import Flask, render_template, request

# 创建Flask应用程序实例
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=360)


# Flask中定义路由是通过装饰器实现的
@app.route('/')
def index_page():
    # return render_template("index.html")
    return render_template("功能验证版主页.html")


@app.route('/search_id', methods=['GET', 'POST'])
def search_id():
    """
    使用id搜索对应的图片
    1. 路由需要有get和post两种请求方式 --> 需要判断请求方式
    2. 获取请求的参数
    3. 判断参数是否填写，参数是否有效
    4.返回对应的图片
    """
    if request.method == "POST":
        image_id = request.form.get("id")
        if image_id:
            try:
                image_id = int(image_id)
                if 0 < image_id < 20:
                    res = "static/images/" + str(image_id) + ".png"
                    return render_template("图片页.html", show_img=res)
            except:
                pass
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
