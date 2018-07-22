# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:25:46 2018

@author: Angus
"""

import os

def getfirmware(current_version=None, request_verstion=None):
    directory = os.getcwd() + '/firmware'  # 假设在当前目录
    firmfile = 'firmware.bin'
    
    if request_verstion:
        firmfile = 'esp8266_httpUpdate-' + request_verstion + '.bin'
    elif current_version:
        if current_version == '0.0.1':
            firmfile = 'esp8266_httpUpdate-0.0.2.bin'
        elif current_version == '0.0.2':
            firmfile = 'esp8266_httpUpdate-0.0.3.bin'
        elif current_version == '0.0.3':
            firmfile = ''
    else:
        firmfile = 'esp8266_httpUpdate-0.0.1.bin'

    return directory, firmfile

