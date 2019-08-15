# -*- coding: utf-8 -*-
"""
File Name：     pyinstaller_test
Description :
Author :       meng_zhihao
date：          2018/11/29
"""
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['congfujiance.py', '-F','-w'] # 容易被360干掉 干掉之后取木马查杀恢复区捞回来再信任
    # 图标修改后不显示可能是windows缓存，换个名字就显示了
    # opts = ['async_test.py', '-F', '-w']
    # opts = ['TargetOpinionMain.py', '-F', '-w', '--icon=TargetOpinionMain.ico','--upx-dir','upx391w']
    run(opts)




