#-*- coding=utf-8 -*-
#@Time : 2020/4/6 8:31
#@Author : kakonose
#@File ：testSpider.py
#@Software: PyCharm
from bs4 import BeautifulSoup #网页解析，获取数据
import re #正则表达式，进行文字匹配
import urllib.request #制定URL，获取网页数据
import urllib.error
from urllib import parse
import xlwt #进行EXCEL操作
import sqlite3 #进行SQLite数据库操作
'''
制作流程
1爬取数据:          spider.py
爬取列表
取详情
2数据保存           51job.db
保存列表
保存详情
3搭建框架           app.py  路由  templates页面 static素材 (图片、CSS、 js)
前端页面
列表显示
表单制作
4制作图表   echarts.js \wordcloud
Echarts
-柱形图
-饼形图
WordCloud
'''
# https://search.51job.com/list/160200,000000,0000,00,9,99,Java,2,1.html

kw = input("请输入您要搜索的岗位关键字：")
keyword = parse.quote(parse.quote(kw))
# pageNum = 1
jobData = {} #每一个记录，是一个列表，每公列表中有多个键值对
#{"linK":"http://www.123.com", "cname":"XXX","iname":"pythonXXXX","salary,":"20000/月"}
jobList = [] #所有的工作岗位信息,放到列表中，每个列表的元素，是上面的字典 [{},{},{}]



#主流程
def main():
    # initDB()
    #循环获得对应job list网页地址
    for i in range(1,20):
        url = "https://search.51job.com/list/160200,000000,0000,00,9,99," + keyword + ",2," + str(i) + ".html"
        pagelist = getLink(url)  # 爬取1个列表页，获取该页的全部岗位链接
        if len(pagelist) == 0: # 如果链接为空的话，打断
            break
        for jobPage in jobList:
            getData(jobPage)#一个详情页的连接
    print(datalist)
    # saveData()

#得到指定一个URL的网页内容
def askURL(url):
    headers = {#模拟浏览器头部信息,向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }#用户代理:表示告返豆瓣服务器:我们是什么类型的机器: 浏览器(本质上是告诉浏览器，我们可以接收什么水平的文件内容)
    request = urllib.request.Request(url,headers=headers)
    html = ""
    try:
        res = urllib.request.urlopen(request)
        html = res.read().decode("gbk")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#获取到所有的工作岗位连接
def getLink(url):
    joblink = []
    html = askURL(url)#获取列表页
    # print(html)
    # print(url)
    bs = BeautifulSoup(html, "html.parser")

    resultlist = bs.select("#resultList")
    eldiv = bs.select(".el > .t1 > span > a")  # el类下 t1类下 span标签下 a标签 其实可以直接通过选择器看
    # print(eldiv)
    for link in eldiv:
        joblink.append(link["href"])
        jobList.append({"link":link["href"]})
        # print(link["href"])# 键为href的value
        # print(link["title"])# 键为title的value
        # print(link.text.strip())  # 标签中的文字
    return []

def getData(jobPage):
    jobHtml = askURL(jobPage) #获取详情页
    bs = BeautifulSoup(jobHtml,"html.parser")
    #只判断给哪一个详情页做捕获，基于该链接的link键，进行爬取
    for job in jobList:
        if jobPage == job["link"]:
            jnames = bs.select(".cn > h1")
            job["title"] = jnames["title"][0]# 将岗位标题放入我们的字典中
            cnamelist = bs.select(".cname a")# 公司名称
            jobMsgList = bs.select(".job_msg > p")#工作猫述
            jobMsgStr = ""
            for str in jobMsgList:
                jobMsgStr = jobMsgStr + str.text
            days = bs.select(".ltype")
            info = days[0]["title"].split("|")
            # for inf in info:
            #     print(inf.strip())


if __name__ == "__main__":
    # main()
    askURL("https://jobs.51job.com/dengfengshi/121155155.html?s=01&t=0")