import pymysql
import pymysql.cursors

def sign(uname, password):
    results = None
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='bulletinboard')
    cur = conn.cursor()
    results = cur.execute("select uname from user")
    if uname in results:
        return "이미 해당 유저가 있습니다."
    else:
        cur.execute("insert into user (uname, password) values(%s, %s)".format(uname, password))
    conn.commit()
    conn.close

def delete(status):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='bulletinboard')
    cur = conn.cursor()
    cur.execute("delete from board where status = '{0}'".format(status))
    conn.commit()
    conn.close

def create(status):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='bulletinboard')
    cur = conn.cursor()
    cur.execute("insert into board(status) values('{0}')".format(status))
    conn.commit()
    conn.close