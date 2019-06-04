import pymssql

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

def mssql_connect():
    ms = MSSQL(host="192.168.1.16",user="sa",pwd="p@ssw0rd",db="GN")
    return ms

def mssql_select():
    result = mssql_connect().ExecQuery("select CodeConfigId from T_CODECONFIG where Deleted=0")
    uid_list = []
    for i in result:
        uid_list.append(i[0])
    return uid_list

L = mssql_select()

def random_from_list():
    from random import choice
    return choice(L)
