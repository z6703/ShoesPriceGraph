"""
@Project -> File   : flaskServer -> app.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/3/31 16:05
@Desc   :
"""
from datetime import timedelta

from flask import Flask, render_template, request
from pyecharts import options as opts
from pyecharts.charts import Line
import controller

# 创建Flask应用程序实例
app = Flask(__name__)
app_controller = controller.Controller()
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=360)
app.DEBUG=True
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


@app.route('/search_id', methods=['GET', 'POST'])
def search_id():
    """
    使用id搜索对应的图片
    1. 路由需要有get和post两种请求方式 --> 需要判断请求方式
    2. 获取请求的参数
    3. 判断参数是否填写，参数是否有效
    4.返回对应的图片和价格折线图
    """
    if request.method == "POST":
        image_id = request.form.get("id")
        if image_id:
            try:
                image_id = int(image_id)
                if 0 < image_id < 20:
                    res = "static/images/" + str(image_id) + ".png"

                    return render_template("img_chart.html", show_img=res, chart_id=image_id)
            except:
                pass
    return render_template("index.html")


@app.route('/line_chart/<chart_id>', methods=['GET', 'POST'])
def draw_line_chart(chart_id):
    date, price = app_controller.get_chart(shoes_id=1, color_id=1, size=1)
    l = line_base(date, price)
    return l.dump_options_with_quotes()


@app.route('/search_test', methods=['GET', 'POST'])
def search_test():
    """
    使用名称搜索对应的鞋
    1. 路由需要有get和post两种请求方式 --> 需要判断请求方式
    2. 获取请求的参数
    3. 判断参数是否填写，参数是否有效
    4. 返回匹配到的搜索结果
    """
    if request.method == "POST":
        image_id = request.form.get("id")
        return render_template("search_result.html",
                               search_res=["/static/images/1.png", "/static/images/2.png", "/static/images/3.png",
                                           "/static/images/4.png", "/static/images/5.png"])


# @app.route('/<int:id>/mainpage', methods=('GET', 'POST'))
# def mainpage(id):
#     root_dir = os.path.abspath(os.path.dirname(__file__))
#     img_path = root_dir + '\static' + '\images'  # 图片文件存储在static文件夹下的images文件夹内
#     files = os.listdir(img_path)  # 获取图片文件名字
#     if id == len(files):
#         id = 0
#     file = "/static/images/" + files[id]
#     return file

def line_base(date: list, price: list) -> Line:
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


if __name__ == '__main__':
    app.run(debug=True)
