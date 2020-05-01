import os
from socket import socket, AF_INET, SOCK_STREAM
from chinese_speech_recognition.general_function.file_wav import *
import json as js
import requests

# file_name = 'chinese_speech_recognition/demovedio/A2_10.wav'
# sock = socket(AF_INET, SOCK_STREAM)
# sock.connect(('127.0.0.1',50008))
# sock.send(str.encode(file_name))
#
# data = sock.recv(4096)
# print('分析结果：',bytes.decode(data))

if __name__ == "__main__":
    file_name = 'chinese_speech_recognition/demovedio/A2_10.wav'

    url = 'http://127.0.0.1:8084/api/speech_recognize'

    with requests.request("POST", url=url, data=js.dumps({'file': file_name}), stream=True) as report:
        result_response = js.loads(report.content)
        print(time.asctime(time.localtime(time.time())))
        print(result_response["result"])
        print(result_response["status"])