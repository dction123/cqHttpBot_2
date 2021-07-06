#!/usr/bin/env python
# coding:utf8
"""
__time__ = '2021/7/5 22:22'
__author__ = 'Liang'
签到系统结构体
"""
"""
签到系统需要 参数
签到人的qq号 ‘’
签到日期 time  2021-07-05 22:37:32
签到状态 status 0签到 1未签到

"""
import mysql.connector as conn
import db_conn
import time


class SingUser:
    def __init__(self, qq, time, status):
        self.qq = qq
        self.time = time
        self.status = status
        print(self.qq)
        print(self.time)
        print(self.status)


def insert_singUser(user: SingUser, db: conn):
    sql = 'insert into sing_in (qq_id,time,status) values (%s,%s,%s)'
    values = (user.qq, user.time, user.status)
    mycursor = db.cursor()
    mycursor.execute(sql, values)
    db.commit()
    print(mycursor.rowcount, "记录插入成功。")
    db.close()


def check_sing_qq(qq_id, db: conn):
    """


    :param qq_id:
    :param db:
    :return: 返回查询结果 如果 已签到 返回真 未签到返回假
    """
    sql = 'select time,status from sing_in where qq_id =' + qq_id
    mycursor = db.cursor()
    mycursor.execute(sql)
    results = mycursor.fetchall()
    print(results)
    t1 = results[0][0]
    t2 = time.strftime("%Y-%m-%d", time.localtime())
    print(t1)
    print(t2)
    print(t2.__eq__(t1))

    # if len(results)!=0:
    #     # 存在该用户 判断签到状态
    #     if results[0][0] == 0:
    #         return True
    #     elif results[0][0] == 1:
    #         return False
    #





if __name__ == '__main__':
    # t = time.strftime("%Y-%m-%d", time.localtime())[0]
    t = time.localtime()
    print(t)
    # user = SingUser('666', t, 1)
    db = db_conn.getConnection()
    # insert_singUser(user, db)
    status = check_sing_qq('666',db)
    print('签到状态：',status)

