import pymysql
import pymysql.cursors

conn = pymysql.connect(host='localhost', user='root', password='1234', db='bb')
cur = conn.cursor()

def data():
    cur.execute("select title, creater, date, saw, id from board order by date desc")
    datas = cur.fetchall()
    return datas

def view(id):
    cur.execute(f"select title, creater, details, id from board where id = '{id}'")
    datas = cur.fetchall()
    return datas

def saw(id):
    cur.execute(f"update board set saw = saw + 1 where id = '{id}'")
    conn.commit()

def search(search):
    cur.execute(f"select title, creater, date, saw, id from board where title like '%{search}%' order by date desc")
    datas = cur.fetchall()
    return datas

def create(title, creater, details):
    cur.execute(f"insert into board(title, creater, details, saw, date) values('{title}', '{creater}', '{details}', 0, now())")
    conn.commit()

def update(id, ntitle, details):
    cur.execute(f"update board set title = '{ntitle}', details = '{details}' where id = '{id}'")
    conn.commit()

def delete(id):
    cur.execute(f"delete from board where id = '{id}'")
    conn.commit()