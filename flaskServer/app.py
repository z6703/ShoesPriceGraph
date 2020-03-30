from flask import Flask, render_template

# 创建Flask应用程序实例
app = Flask(__name__)


# Flask中定义路由是通过装饰器实现的
@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template("1.html")


@app.route('/orders/<int:order_id>')
def check_order(order_id):
    return "查询" + order_id


if __name__ == '__main__':
    app.run(debug=True)
