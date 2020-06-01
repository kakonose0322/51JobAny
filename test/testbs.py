#-*- coding=utf-8 -*-
#@Time : 2020/4/6 9:06
#@Author : kakonose
#@File ：testbs.py
#@Software: PyCharm
from bs4 import BeautifulSoup

'''
html = open("joblist.html","r")
bs = BeautifulSoup(html,"html.parser")

resultlist = bs.select("#resultList")
eldiv = bs.select(".el > .t1 > span > a")# el类下 t1类下 span标签下 a标签 其实可以直接通过选择器看
#print(eldiv)
for link in eldiv:
    # print(link["href"])# 键为href的value
    # print(link["title"])# 键为title的value
    print(link.text.strip())# 标签中的文字
'''

html = open("jobcontent.html","r")
bs = BeautifulSoup(html,"html.parser")
jname = bs.select(".cn > h1")
days = bs.select(".ltype")
info = days[0]["title"].split("|")
for inf in info:
    print(inf.strip())
#print(eldiv)
# for name in jname:
#     # print(link["href"])# 键为href的value
#     # print(link["title"])# 键为title的value
#     print(name["title"])# 标签中的文字
# for day in days:
#     print(day["title"])