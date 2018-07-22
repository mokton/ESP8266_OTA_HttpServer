# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 21:57:18 2018

@author: Angus
"""

from __future__ import print_function
import os


# 字节bytes转化kb\m\g
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        print("传入的字节格式不对")
        return "Error"

    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%fG" % (G)
        else:
            return "%fM" % (M)
    else:
        return "%fkb" % (kb)


# 获取文件大小
def getDocSize(path):
    try:
        size = os.path.getsize(path)
        return size #formatSize(size)
    except Exception as err:
        print(err)


# 获取文件夹大小
def getFileSize(path):
    sumsize = 0
    try:
        filename = os.walk(path)
        for root, dirs, files in filename:
            for fle in files:
                size = os.path.getsize(path + fle)
                print(size, path + fle)
                sumsize += size
        return sumsize #formatSize(sumsize)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    print(getDocSize("C:\\Users\\Angus\\AppData\\Local\\Temp\\arduino_build_185343\\BasicOTA.ino.bin"))
    # 1006.142578kb
    #print(getFileSize("C:\\Users\\Angus\\AppData\\Local\\Temp\\arduino_build_185343\\"))
    # 111.856756M