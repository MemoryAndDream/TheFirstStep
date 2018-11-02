# -*- coding: utf-8 -*-
"""
File Name：     zhuce
Description :
Author :       meng_zhihao
date：          2018/11/2
"""
import win32api
print win32api.GetVolumeInformation("C:\\")[1]
