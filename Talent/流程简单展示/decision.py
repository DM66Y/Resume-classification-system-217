# -*- coding: utf-8 -*-
# @Time    : 2020/3/21
# @Author  : Li Yue
# @FileName: receive_server.py
# @Software: PyCharm
#收发器，将收到图片、文字或者视频存至数据库

import sys
import os


sys.path.append(os.getcwd())
from flask import Flask, request, jsonify
import requests
import time
import json as js
import pymysql
import logging

from file_type import file_type

image_info = []
rec_element = []

application = Flask(__name__)
logger = logging.getLogger(__name__)

"""
        收发器：将收到文字音频存至数据库
"""

@application.route('/')
def index():
    return "index(没有页面)"

@application.route('/api/decision', methods=['GET', 'POST'])
def uplaod_file():
    if request.method == 'POST':
        start = time.time()
        user_id = js.loads(request.data)["user_id"]
        file_num = js.loads(request.data)["file_num"]
        file = js.loads(request.data)["file_info"]
        # print(user_id)
        # print(file_num)

        num = len(js.loads(request.data)["file_info"])
        # print(num)


        if file_type(file) == "wav":
            with requests.request("POST",url='http://127.0.0.1:4014/api/facialrec',data=js.dumps({'user_id': user_id, 'file_num': file_num, 'file_info': file}),stream=True) as report:
                result_response = js.loads(report.content)['result']
                print(result_response)


        elif file_type(file) == "mp4":

            with requests.request("POST", url='http://127.0.0.1:4014/api/facialrec',
                              data=js.dumps({'user_id': user_id, 'file_num': file_num, 'file_info': file, 'file_type':'video'}),
                              stream=True) as report:
                result_response = js.loads(report.content)['result']
                print(result_response)
        elif file_type(file) == "jpg" or file_type(file) == "png":
            with requests.request("POST", url='http://127.0.0.1:4014/api/facialrec',
                              data=js.dumps({'user_id': user_id, 'file_num': file_num, 'file_info': file, 'file_type':'image'}),
                              stream=True) as report:
                result_response = js.loads(report.content)["result"]
                print(result_response)




        json = {
                    "status": 1
                }
        return jsonify(json)





if __name__ == '__main__':
    application.run(host="127.0.0.1", port=4011, debug=True)


