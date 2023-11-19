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
        return "회원가입이 완료되었습니다."
    conn.commit()
    conn.close

def delete(bid):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='bulletinboard')
    cur = conn.cursor()
    cur.execute("delete from board where bid = %d".format(bid))
    conn.commit()
    conn.close

def create(uid, title, detail):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='bulletinboard')
    cur = conn.cursor()
    cur.execute("insert into board(uid, title, detail) values(%d, %s, %s)".format(uid, title, detail))
    conn.commit()
    conn.close
    
def update(bid, title, detail):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='bulletinboard')
    cur = conn.cursor()
    cur.execute("update board set title = %s, detail = %s where bid = %d".format(title, detail, bid))
    conn.commit()
    conn.close
    
def login(uname, password):
    check = None
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='bulletinboard')
    cur = conn.cursor()
    check = cur.execute("select uname, password from user")
    if uname not in check or password not in check:
        return "이름이나 비밀번호가 일치하지 않습니다."
    else:
        return "로그인 성공"
    conn.commit()
    conn.close