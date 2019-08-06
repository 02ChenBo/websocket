#import pymysql
#
# connect = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='',
#     db='cloud_note',
#     charset='utf8'
# )
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# import MySQLdb
# def mySql(ss):
#     # 打开数据库连接
#     db = MySQLdb.connect("localhost","root","","cloud_note")
#
#     # 使用cursor()方法获取操作游标
#     cursor = db.cursor()
#
#     # 使用execute方法执行SQL语句
#     cursor.execute(ss)
#
#     # 使用 fetchone() 方法获取一条数据库。
#     data = cursor.fetchone()
#
#     #print ("Database version : %s " % data)
#
#     # 关闭数据库连接
#     db.close()
#     return data;
#
# ss = "SELECT VERSION()";
# str = mySql(ss);
# print(str);
