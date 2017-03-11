#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : database.py
# @Author: fuqumao
# @Date  : 2017-03-11
# @Desc  :封装链接数据库模块

import pymssql


class MSSQL:
    """
    #初始化函数
    #参数host:数据库地址,sql_user:数据库用户,
    #数据库密码:sql_pwd,数据库名称:database_name
    """

    def __init__(self, host, sql_user, sql_pwd, database_name):
        self.host = host
        self.sql_user = sql_user
        self.sql_pwd = sql_pwd
        self.database_name = database_name

    """
    #获取数据连接函数
    """

    def getDbConection(self):
        '''
        如果和本机数据库交互，只需修改链接字符串
        conn=pymssql.connect(host='.',database='Michael')
        '''
        conn = pymssql.connect(host=self.host, user=self.sql_user, password=self.sql_pwd, database=self.database_name)

        return conn

    """
       #获取数据连接函数
    """

    def getDBCursor(self):
        cur = self.getDbConection().cursor()

        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    # def execQuery(self,sql):

# cur.execute('select top 1 * from [dbo].[a_employee_mi]')
# # 如果update/delete/insert记得要conn.commit()
# # 否则数据库事务无法提交
# # print (cur.fetchall())
# rows = cur.fetchall()
# for row in rows:
#     # s = ''
#     # s = ','.join(row)
#     print row.__str__()
#     # for i in range(0, len(row)):
#     #     s = s + row[i]
#     # print s
# cur.close()
#
# conn.close()

if __name__ == '__main__':
    mssql = MSSQL("localhost", "hissql", "86128613@Rmyy", "sdyymz")
    try:
        cur = mssql.getDBCursor()
        cur.execute('select top 1 code,* from a_employee_mi')
        rows = cur.fetchall()
        for row in rows:
            print row.__str__()
            # print row['code']
        cur.close

    except Exception, e:
        print(e.message)
