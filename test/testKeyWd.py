#-*- coding=utf-8 -*-
#@Time : 2020/4/6 8:59
#@Author : kakonose
#@File ：testKeyWd.py
#@Software: PyCharm

from urllib import parse

keyword = parse.quote("大数据")
newKW = parse.quote(keyword)# 二次编码,主要特征为一次编码基础上，多了很多%25
print(newKW)