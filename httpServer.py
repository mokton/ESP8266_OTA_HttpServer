# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:41:18 2018

@author: Angus
"""

from __future__ import print_function

import os
import firmwarePath
from auto_reload import auto_reload
from filesize import getDocSize

from flask import Flask, request, url_for
from flask import send_file, send_from_directory
from flask import render_template
app = Flask(__name__)

#    Esp8266 httpUpdate Headers
#    X-Esp8266-Sta-Mac: 5C:CF:7F:D9:F9:30
#    X-Esp8266-Ap-Mac: 5E:CF:7F:D9:F9:30
#    User-Agent: ESP8266-http-Update
#    Connection: close
#    X-Esp8266-Free-Space: 2875392
#    X-Esp8266-Chip-Size: 4194304
#    X-Esp8266-Sdk-Version: 1.3.0
#    Host: 192.168.1.101
#    X-Esp8266-Sketch-Size: 268100
#    X-Esp8266-Version: 0.0.2

fwdir = os.getcwd() + '/firmware'

@app.route('/')
def rootpage():
    return 'Esp8266 Firmware Updater'

@app.route('/firmware/', methods=['GET'])
@app.route('/firmware/<board>', methods=['GET'])
def firmware(board=None):
#    directory = os.getcwd() + '/firmware'  # 假设在当前目录
#    firmfile = 'firmware.bin'
    auto_reload(['firmwarePath'])
    directory, firmfile = fwdir, ''
    if board:
        request_version = request.args.get('version')
        if board.lower() == 'esp8266':
            current_version = request.headers.get('X-Esp8266-Version')
            directory, firmfile = firmwarePath.getfirmware(current_version, request_version)
    else:
        pass
    
#    if current_version:
#        if current_version == '0.0.1':
#            firmfile = 'esp8266_httpUpdate-0.0.2.bin'
#        elif current_version == '0.0.2':
#            firmfile = 'esp8266_httpUpdate-0.0.3.bin'
#        elif current_version == '0.0.3':
#            firmfile = ''
#    else:
#        firmfile = 'esp8266_httpUpdate-0.0.1.bin'
        
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    return send_from_directory(directory, firmfile, as_attachment=True)
    
@app.route('/hasNewfirmware/', methods=['GET'])
def hasNewfirmware():
    # print(request.headers)
    directory = fwdir  # 假设在当前目录
    f = open(directory + '/new.txt')
    hasNew = f.read()
    f.close()
    hasNew = hasNew[0]
    if hasNew != '1':
        hasNew = '0'
    return hasNew
    
@app.route('/firmware-list/<board>', methods=['GET'])
def firmware_list(board=None):
    filelist = []
    filefullpath = ''
    n = 0
    try:
        for root, dirs, files in os.walk(fwdir):  
            for f in files:
                if os.path.splitext(f)[0][0:len(board)] == board and os.path.splitext(f)[1] == '.bin':
                    filefullpath = os.path.join(root, f)
                    #print(os.path.splitext(f)[0].split('-'))
                    n += 1
                    filelist.append((n, f, getDocSize(filefullpath), '/firmware/esp8266?version=' + os.path.splitext(f)[0].split('-')[1]))
    except:
        pass
    return render_template('esp8266fw.html', files = filelist, board = board)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6051)

