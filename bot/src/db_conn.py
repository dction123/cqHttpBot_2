#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/7/5 22:39'
__author__ = 'Liang'
"""

import mysql.connector as conn


def getConnection():
    mydb = conn.connect(
        host="47.98.101.50",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="lbwnb123",  # 数据库密码
        database="robot"  # 表示要使用那个库
    )

    # print(mydb)
    # mycursor = mydb.cursor()  # 数据库游标

    return mydb

