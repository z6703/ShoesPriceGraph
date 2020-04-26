workers = 3  # 定义同时开启的处理请求的进程数量，根据网站流量适当调整

worker_class = "gevent"  # 采用gevent库，支持异步处理请求，提高吞吐量

bind = "0.0.0.0:5000"  # 监听端口

daemon = True  # 设置守护进程

loglevel = 'debug'  # 设置日志记录水平

errorlog = '/logs/gunicorn_error.log'  # 设置错误信息日志路径

accesslog = '/logs/gunicorn_access.log'  # 设置访问日志路径
