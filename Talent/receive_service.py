# -*- coding: utf-8 -*-
# @Time    : 2020/3/21
# @Author  : Li Yue
# @FileName: receive_server.py
# @Software: PyCharm
#收发器，将收到图片、文字或者视频存至数据库

import sys
import os


sys.path.append(os.getcwd())
import numpy as np
from flask import Flask, request, jsonify
import requests
import time
import json as js
import pymysql
import logging
from flask import render_template

from file_type import file_type

image_info = []
rec_element = []

application = Flask(__name__)
logger = logging.getLogger(__name__)

"""
        收发器：将从前端收到文件保存至本地，再根据其类别把它们存至数据库
"""

@application.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@application.route('/api/upload', methods=['GET', 'POST'])
def uplaod_file():

    if request.method == 'POST':

        # 设置存放文件的地址，并保存文件至本地
        UPLOAD_FOLDER = 'file_dir/'
        file_dir = os.path.join(os.getcwd(), UPLOAD_FOLDER)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        print(file_dir)

        # print(request.files)
        # print(request.files['file'])

        file = request.files['file']
        filename = request.files['file'].filename
        file.save(UPLOAD_FOLDER + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(np.random.randint(0, 9999)) + filename)
        print(filename + "存储成功")

        file_path = UPLOAD_FOLDER + str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(np.random.randint(0, 9999)) + filename

        print("文件存储在" + file_path)

        # 正式版把注释代码取出即可
        result = '666'
        # 返回模型的结果到前端
        return result


        # if(file_path.split('.')[-1] == 'docx'):
        #     print(filename + '送入马飞模型')
        #     url = 'http://127.0.0.1:8083/api/resume_classify'
        #     with requests.request("POST", url=url, data=js.dumps({'file': file_path}), stream=True) as report:
        #         result_response = js.loads(report.content)
        #         print(time.asctime(time.localtime(time.time())))
        #         print(result_response["result"])
        #         print(result_response["status"])
        #         result = result_response["result"]
        #
        # elif(file_path.split('.')[-1] == 'wav'):
        #     print(filename + '送入英飞模型')
        #     url = 'http://127.0.0.1:8083/api/resume_classify'
        #     with requests.request("POST", url=url, data=js.dumps({'file': file_path}), stream=True) as report:
        #         result_response = js.loads(report.content)
        #         print(time.asctime(time.localtime(time.time())))
        #         print(result_response["result"])
        #         print(result_response["status"])
        #         result = result_response["result"]
        #
        #
        # elif (file_path.split('.')[-1] == 'mp4' or file_path.split('.')[-1] == 'jpg' or file_path.split('.')[-1] == 'png'):
        #     print(filename + '送入猪哥模型')
        #     url = 'http://127.0.0.1:8083/api/resume_classify'
        #     with requests.request("POST", url=url, data=js.dumps({'file': file_path}), stream=True) as report:
        #         result_response = js.loads(report.content)
        #         print(time.asctime(time.localtime(time.time())))
        #         print(result_response["result"])
        #         print(result_response["status"])
        #         result = result_response["result"]
        #
        # else:
        #     print(filename + '是非法的文件类型！')




        # filename = file.filename
        # file.save(os.path.join(UPLOAD_FOLDER, filename))
        # print(file.filename + '已存入本地')

        # start = time.time()
        # user_id = js.loads(request.data)["user_id"]
        # file_num = js.loads(request.data)["file_num"]
        # file_info = js.loads(request.data)["file_info"]
        # # print(user_id)
        # # print(file_num)
        #
        # num = len(js.loads(request.data)["file_info"])
        # # print(num)
        #
        # if (file_num == num):
        #     #对每个文件进行遍历，分三类存储进数据库
        #     for i in range(file_num):
        #         file = file_info[i]["file_obj"]
        #         conn = pymysql.connect(host="localhost", port=3306, user="root", password="root",
        #                                database="talent_1",
        #                                charset="utf8")
        #         cur = conn.cursor()
        #         #英组
        #         if file_type(file) == "wav":
        #             mydict = {}
        #             mydict["file_id"] = js.loads(request.data)["file_info"][i]["file_id"]
        #             mydict["file"] = file
        #             print(mydict["file"])
        #             conn.ping(reconnect=True)
        #             sql = "INSERT INTO file_store(file_id, user_id, file_wav, is_used) VALUES ('%s','%s','%s','%s')" \
        #                   % (mydict["file_id"], user_id, mydict["file"], 1)
        #             cur.execute(sql)
        #             conn.commit()
        #             print("wav数据存储完成")
        #             conn.close()
        #
        #         #猪组
        #         elif file_type(file) == "mp4":
        #             mydict = {}
        #             mydict["file_id"] = js.loads(request.data)["file_info"][i]["file_id"]
        #             mydict["file"] = file
        #             print(mydict["file"])
        #             conn.ping(reconnect=True)
        #             sql = "INSERT INTO file_store(file_id, user_id, file_mp4, is_used) VALUES ('%s','%s', '%s', '%s')" \
        #                   % (mydict["file_id"], user_id, mydict["file"], 1)
        #             cur.execute(sql)
        #             conn.commit()
        #             print("mp4数据存储完成")
        #             conn.close()
        #
        #         elif file_type(file) == "jpg" or file_type(file) == "png":
        #             mydict = {}
        #             mydict["file_id"] = js.loads(request.data)["file_info"][i]["file_id"]
        #             mydict["file"] = file
        #             print(mydict["file"])
        #             conn.ping(reconnect=True)
        #             sql = "INSERT INTO file_store(file_id, user_id, file_img, is_used) VALUES ('%s','%s', '%s', '%s')" \
        #                   % (mydict["file_id"], user_id, mydict["file"], 1)
        #             cur.execute(sql)
        #             conn.commit()
        #             print("img数据存储完成")
        #             conn.close()
        #
        #         #马组
        #         elif file_type(file) == "docx":
        #             mydict = {}
        #             mydict["file_id"] = js.loads(request.data)["file_info"][i]["file_id"]
        #             mydict["file"] = file
        #             print(mydict["file"])
        #             conn.ping(reconnect=True)
        #             sql = "INSERT INTO file_store(file_id, user_id, file_doc, is_used) VALUES ('%s','%s', '%s', '%s')" \
        #                   % (mydict["file_id"], user_id, mydict["file"], 1)
        #             cur.execute(sql)
        #             conn.commit()
        #             print("word数据存储完成")
        #             conn.close()
        #
        #         else:
        #             print(file.split('/')[-1] + "不是支持位置的数据类型!")
        #             conn.close()
        #
        #     print(time.time() - start)

    # else:
    #     with requests.request("POST", url="http://127.0.0.1:8070/api/upload",data=js.dumps({"ocr_status": "0", "user_id": user_id, "client_code": "接收失败，请重新发送"}), stream=True)as rep:
    #         r = rep.content
    #     json = {
    #         "status": 0
    #     }
    #     return jsonify(json)




if __name__ == '__main__':
    application.run(host="localhost", port=8080, debug=True)


