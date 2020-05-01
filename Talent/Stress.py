# -*- coding: utf-8 -*-
# @Time    : 2020/4/13
# @Author  : Li Yue
# @FileName: Stress.py
# @Software: PyCharm
#收发器，将收到图片、文字或者视频存至数据库

import numpy as np
import cv2
import os
import time
import json as js
import requests
import base64


'''
Stress Test 压力测试
'''

# 公司方的测试，发送json字段给马飞
def Stress_Test_Company(num):

    url = 'http://39.104.200.184:6060/api/requirement'   # destination of data

    requirement = [
        {
            'id': str(1 + (num - 1)*6),
            'company': '腾讯控股',
            'job': '教师',
            'age': '23-35',
            'gender': '不限',
            'education': '研究生',
            'salary': '7500',
            'city': '昆山',
            'area': '玉山镇',
            'skill': '无',
            'experience': '从事过教育行业者优先',
            'Extraversion': '25%',
            'Introversion': '0%',
            'Sensing': '15%',
            'iNtuition': '15%',
            'Thingking': '20%',
            'Feeling': '10%',
            'Perceiving': '5%',
            'Judging': '10%'
        },

        {
            'id': str(2 + (num - 1)*6),
            'company': '腾讯控股',
            'job': '安保人员',
            'age': '23-40',
            'gender': '男',
            'education': '大专',
            'salary': '6000',
            'city': '昆山',
            'area': '八城镇',
            'skill': '无',
            'experience': '从事过安保行业者优先',
            'Extraversion': '0%',
            'Introversion': '25%',
            'Sensing': '20%',
            'iNtuition': '10%',
            'Thingking': '15%',
            'Feeling': '10%',
            'Perceiving': '10%',
            'Judging': '10%'
        },

        {
            'id': str(3 + (num - 1)*6),
            'company': '新东方教育',
            'job': '教师',
            'age': '22-30',
            'gender': '女',
            'education': '研究生',
            'salary': '9000',
            'city': '昆山',
            'area': '千灯镇',
            'skill': '无',
            'experience': '从事过对外汉语教学者优先',
            'Extraversion': '30%',
            'Introversion': '0%',
            'Sensing': '15%',
            'iNtuition': '10%',
            'Thingking': '25%',
            'Feeling': '5%',
            'Perceiving': '5%',
            'Judging': '10%'
        },

        {
            'id': str(4 + (num - 1)*6),
            'company': '可口可乐',
            'job': '销售代表',
            'age': '25-45',
            'gender': '不限',
            'education': '本科',
            'salary': '8500',
            'city': '昆山',
            'area': '陆家镇',
            'skill': '无',
            'experience': '从事过市场行业者优先',
            'Extraversion': '35%',
            'Introversion': '0%',
            'Sensing': '10%',
            'iNtuition': '20%',
            'Thingking': '15%',
            'Feeling': '10%',
            'Perceiving': '5%',
            'Judging': '10%'
        },

        {
            'id': str(5 + (num - 1)*6),
            'company': '阿里巴巴',
            'job': '教师',
            'age': '23-35',
            'gender': '不限',
            'education': '本科',
            'salary': '9500',
            'city': '昆山',
            'area': '巴城镇',
            'skill': '无',
            'experience': '从事过教育行业者优先',
            'Extraversion': '25%',
            'Introversion': '0%',
            'Sensing': '20%',
            'iNtuition': '10%',
            'Thingking': '20%',
            'Feeling': '10%',
            'Perceiving': '5%',
            'Judging': '10%'
        },

        {
            'id': str(6 + (num - 1)*6),
            'company': '网易教育',
            'job': '教师',
            'age': '23-35',
            'gender': '不限',
            'education': '研究生',
            'salary': '9000',
            'city': '昆山',
            'area': '巴城镇',
            'skill': '无',
            'experience': '从事过教育行业者优先',
            'Extraversion': '20%',
            'Introversion': '0%',
            'Sensing': '15%',
            'iNtuition': '15%',
            'Thingking': '25%',
            'Feeling': '5%',
            'Perceiving': '10%',
            'Judging': '10%'
        }

    ]

    for r in requirement:
        try:
            requests.post(url=url, data=r)
            print(time.asctime(time.localtime(time.time())))
            print("发送成功")

        except:
            print("发送失败！")



if __name__ == '__main__':

    i = 1

    while(True):
        # 马飞测试数据
        Stress_Test_Company(i)

        i = i + 1

        time.sleep(5)
