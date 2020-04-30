import redis

r = redis.Redis(host="172.18.0.2", port=6379, decode_responses=True)

print(r.smembers("blacklist"))

# pkl_file = open('shoes.pkl', 'rb')
# obj = pickle.load(pkl_file)
# print(obj.id)
# print(obj.name)
# for i in obj.color_info:
#     print(i.color_id)
#     print(i.color_name)
#     print(i.img_link)
#
# c = controller.Controller()
# print(c.search_specific_shoes(1))
#
# import logging
# from logging.handlers import RotatingFileHandler
#
# from flask import Flask
#
# # 日至等级的设置
# logging.basicConfig(level=logging.DEBUG)
# # 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
# file_log_handler = RotatingFileHandler("flask.log", maxBytes=1024000, backupCount=10)
# # 设置日志的格式           日志等级     日志信息文件名   行数        日志信息
# formatter = logging.Formatter('%(levelname)s File = %(filename)s Module = %(module)s Func = %(funcName)s Line = %(lineno)d %(message)s')
# # 将日志记录器指定日志的格式
# file_log_handler.setFormatter(formatter)
# # 为全局的日志工具对象添加日志记录器
# logging.getLogger().addHandler(file_log_handler)
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# if __name__ == '__main__':
#     app.debug = True
#     app.run()
