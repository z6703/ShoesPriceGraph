"""
@Project -> File   : flaskServer -> test.py
@IDE    : PyCharm
@Author : Yimeng Cai
@Date   : 2020/3/31 16:56
@Desc   :
"""
import os

root_dir = os.path.abspath(os.path.dirname(__file__))
img_path = root_dir + '\static' + '\images'  # 图片文件存储在static文件夹下的images文件夹内
files = os.listdir(img_path)  # 获取图片文件名字
print(files)
count = 1
for i in files:
    os.rename("static/images/" + i, "static/images/" + str(count) + ".png")
    count += 1
