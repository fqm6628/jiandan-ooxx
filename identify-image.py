#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : identify-image.py
# @Author: fuqumao
# @Date  : 2017-03-11
# @Desc  :识别图片是否已损坏，损坏的话进行标记写入数据库中，由删除脚本定时进行清理

import Image
import sys
import database
import os


class IdentifyImage():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def identify_image(self, pic_route):
        try:
            im = Image.open(unicode("D:\PythonProject\jiandan-ooxx\第3页第15张.jpg", "utf-8"))
            return True
        except Exception, e:
            return False

    def getImageSize(self, im):
        return im.size

    def GetFileList(self, dir, fileList):
        newDir = dir
        if os.path.isfile(dir):
            fileList.append(dir.decode('gbk'))
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, s)
                self.GetFileList(newDir, fileList)
        return fileList


if __name__ == '__main__':
    idImage = IdentifyImage()
    list = idImage.GetFileList("D:\scrawer_pic", [])
    for e in list:
        print e
