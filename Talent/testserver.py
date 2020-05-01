import os
from socket import socket, AF_INET, SOCK_STREAM
from chinese_speech_recognition.general_function.file_wav import *
import json as js
import requests


if __name__ == "__main__":
    file = 'test_dir/1.docx'

    url = 'http://127.0.0.1:8083/api/resume_classify'

    with requests.request("POST", url=url, data=js.dumps({'file': file}), stream=True) as report:
        result_response = js.loads(report.content)
        print(time.asctime(time.localtime(time.time())))
        print(result_response["result"])
        print(result_response["status"])