# pythontab提醒您注意中文编码问题，指定编码为utf-8
# -*- coding: utf-8 -*-
import filetype

import struct


# 支持文件类型
# 用16进制字符串的目的是可以知道文件头是多少字节
# 各种文件头的长度不一样，少半2字符，长则8字符
def typeList():
    return {
        'ffd8ffe000104a464946': 'jpg',
        '89504e470d0a1a0a0000': 'png',
        '504b0304140006000800': 'docx',
        '00000020667479706d70': 'mp4',
        '52494646e27807005741': 'wav'

    }


# 字节码转16进制字符串
# 字节码转16进制字符串
def bytes2hex(bytes):

    num = len(bytes)

    hexstr = u""
    for i in range(num):
        t = u"%x" % bytes[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


# 获取文件类型
def file_type(filename):
    # print('读文件二进制码中……');

    binfile = open(filename, 'rb')  # 必需二制字读取
    # print('提取关键码……');
    bins = binfile.read(20)  # 提取20个字符
    binfile.close()  # 关闭文件流
    bins = bytes2hex(bins)  # 转码
    bins = bins.lower()  # 小写
    # print(bins);
    tl = typeList() # 文件类型
    ftype = 'unknown'
    # print('关键码比对中……');
    for hcode in tl.keys():
        lens = len(hcode)  # 需要的长度
        if bins[0:lens] == hcode:
            ftype = tl[hcode]
            break
    if ftype == 'unknown':  # 全码未找到，优化处理，码表取5位验证
        bins = bins[0:5];
        for hcode in tl.keys():
            if len(hcode) > 5 and bins == hcode[0:5]:
                ftype = tl[hcode]
                break
    return ftype

if __name__ == '__main__':
    # kind = filetype.guess('test_dir/123.mp4')
    # if kind is None:
    #     print('Cannot guess file type!')
    # else:
    #     print('File extension: %s' % kind.extension)
    #     print('File MIME type: %s' % kind.mime)
    print(file_type("test_dir/1.doc"))
    print(file_type("test_dir/2.wav"))
    print(file_type("test_dir/3.mp4"))
    print(file_type("test_dir/4.txt"))
