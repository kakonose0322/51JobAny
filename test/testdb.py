#-*- coding=utf-8 -*-
#@Time : 2020/4/6 8:33
#@Author : kakonose
#@File ：testdb.py
#@Software: PyCharm
import sqlite3

dbpath = './51job.db'

def init_db(dbpath):
    sql='''
        create table job
        (
        id integer primary key autoincrement,
        job_link text,
        jname text,
        cname varchar,
        area varchar,
        salary numeric,
        educate text,
        info text
        )
    '''
    conn=sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()

# init_db(dbpath)

def saveDataToDB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 5 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql='''
            insert into job(
            info_link, pic_link, cname, ename, score, rated, instroduction, info)
            values (%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()