# -*- coding: utf-8 -*-
# @Time    : 2020/3/21
# @Author  : Li Yue
# @FileName: serve_send.py
# @Software: PyCharm
#从数据库取出数据并发送给模型

"""
    输入user_id   输出该用户在数据库中的文件，包括 file_id 和 file
    根据file的类型，送入三个不同的模型，得到结果，再把结果返回
"""

import pymysql
import sys
import os


sys.path.append(os.getcwd())
from flask import Flask, request, jsonify
import requests
import time
import json as js
import pymysql
import logging

from 简历分类测试.test import classify

application = Flask(__name__)

#数据库配置文件
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'root',
          'db':'talent_1',
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
}

@application.route('/')
def index():
    return "index(没有页面)"


#前端传入的数据有 user_id、file_num、file_info，其中，file_info中包含了file_id和file文件本身
@application.route('/api/data_send', methods=['GET', 'POST'])
def data_send():

    user_id = js.loads(request.data)["user_id"]

    files = []

    # 不断循环，直到数据库里的数据被取光
    conn = pymysql.connect(**config)  # 连接数据库
    cur = conn.cursor()
    # sql语句可优化，简化下方的三个if分支
    sql = "SELECT * FROM file_store WHERE user_id = '%s' AND is_used = 1" % (user_id)
    cur.execute(sql)
    count = cur.rowcount

    try:
        if(count > 0):
            lists = cur.fetchall()
            print(lists)

            # 从数据库取出文件file_id和file本身，并把is_used标志改为0
            for l in lists:
                if(l['file_wav'] != None):
                    # print(l['file_wav'])
                    my_dict = {}
                    my_dict['file_id'] = l['file_id']
                    my_dict['file'] = l['file_wav']
                    files.append(my_dict)

                    sql_mark = "UPDATE file_store SET is_used = 0 WHERE file_id = '%s'" % (l['file_id'])
                    cur.execute(sql_mark)

                elif(l['file_mp4'] != None):
                    # print(l['file_mp4'])
                    my_dict = {}
                    my_dict['file_id'] = l['file_id']
                    my_dict['file'] = l['file_mp4']
                    files.append(my_dict)

                    sql_mark = "UPDATE file_store SET is_used = 0 WHERE file_id = '%s'" % (l['file_id'])
                    cur.execute(sql_mark)

                elif (l['file_img'] != None):
                    # print(l['file_mp4'])
                    my_dict = {}
                    my_dict['file_id'] = l['file_id']
                    my_dict['file'] = l['file_img']
                    files.append(my_dict)

                    sql_mark = "UPDATE file_store SET is_used = 0 WHERE file_id = '%s'" % (l['file_id'])
                    cur.execute(sql_mark)

                else:
                    # print(l['file_doc'])
                    my_dict = {}
                    my_dict['file_id'] = l['file_id']
                    my_dict['file'] = l['file_doc']
                    files.append(my_dict)

                    sql_mark = "UPDATE file_store SET is_used = 0 WHERE file_id = '%s'" % (l['file_id'])
                    cur.execute(sql_mark)

            conn.commit()
            print(files)

            #存放结果
            results = []

            #把得到的文件送入三个模型（待完善）
            for f in files:
                if(f['file'].split('.')[-1] == 'wav'):
                    print(f['file'] + "送入英老师模型")
                    str_1 = "英老师模型结果"
                    my_dict = {}
                    my_dict["user_id"] = user_id
                    my_dict['file_id'] = f['file_id']
                    my_dict['file'] = f['file']
                    my_dict['result'] = str_1
                    results.append(my_dict)

                elif(f['file'].split('.')[-1] == 'mp4' or f['file'].split('.')[-1] == 'jpg' or f['file'].split('.')[-1] == 'png'):
                    print(f['file'] + "送入猪哥模型")
                    str_2 = "猪哥模型结果"
                    my_dict = {}
                    my_dict["user_id"] = user_id
                    my_dict['file_id'] = f['file_id']
                    my_dict['file'] = f['file']
                    my_dict['result'] = str_2
                    results.append(my_dict)

                elif (f['file'].split('.')[-1] == 'docx'):
                    print(f['file'] + "送入马飞模型")
                    url = 'http://127.0.0.1:8083/api/resume_classify'
                    with requests.request("POST", url=url, data=js.dumps({'file': f['file']}), stream=True) as report:
                        result_response = js.loads(report.content)
                        print(time.asctime(time.localtime(time.time())))
                        print(result_response["result"])
                        print(result_response["status"])
                        str_3 = result_response["result"]

                    my_dict = result_response["result"]
                    my_dict["user_id"] = user_id
                    my_dict['file_id'] = f['file_id']
                    my_dict['file'] = f['file']
                    my_dict['result'] = str_3
                    results.append(my_dict)

            print(results)

            #测试用
            for r in results:
                print(r['file'] + "分析结果为" + r['result'])

    except:
        # cur.execute('UPDATE process_st SET process_state="0" where process_name="pro0"')
        # conn.commit()
        conn.close()
        time.sleep(0.1)

    json = {
        "result": results,
        "status": 2
    }
    return jsonify(json)



if __name__ == '__main__':
    application.run(host="0.0.0.0", port=8081, debug=True)