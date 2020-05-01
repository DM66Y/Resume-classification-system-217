# -*- coding: utf-8 -*-
# @Time    : 2020/3/21
# @Author  : Li Yue
# @FileName: stress_test.py
# @Software: PyCharm
#收发器，将收到图片、文字或者视频存至数据库

import numpy as np
import cv2
import os
import time
import json as js
import requests
import base64
from serve_send import data_send

'''
Stress Test 压力测试
'''

def Stress_Test():
    dir_name = r"/home/gpz/Desktop/test/"   #files dirctory
    file_count = 1   #numbers of chosen images per user
    users = 1 #numbers of users
    url = 'http://127.0.0.1:4011/api/decision'   #destination of data
    assert os.path.isdir(dir_name)
    all_files = os.listdir(dir_name)

    for j in range(users):
        files = []
        user_id = "user" + str(j)
        file_num = file_count
        print(user_id)


        for i in range(file_count):

            file = dir_name + all_files[i]


        # try:
        with requests.request("POST", url=url, data=js.dumps({'user_id': user_id, 'file_num': file_num, 'file_info': file}),stream=True) as report:
            result_response = js.loads(report.content)
            print(result_response["status"])
        # except:
        #     print("发送失败！")
        time.sleep(5)

        # 从数据库取出该用户的文件并送入模型
        data_send(user_id)


if __name__ == '__main__':
    Stress_Test()


