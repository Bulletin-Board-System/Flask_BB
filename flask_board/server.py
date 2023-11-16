from flask import Flask, render_template, request
import connectDB

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/create')
def create():
    try:
        uid = request.form['uid']
        title = request.form['title']
        detail = request.form['detail']
        data = connectDB.create(uid, title, detail)
        return data
    except:
        return "error"

@app.route('/login')
def login():
    try:
        uname = request.form['uname']
        password = request.form['password']
        data = connectDB.login(uname, password)
        return data
    except:
        return "error"

@app.route('/sign')
def sign():
    try:
        uname = request.form['uname']
        password = request.form['password']
        data = connectDB.sign(uname, password)
        return data
    except:
        return "error"

@app.route('/delete')
def delete():
    try:
        connectDB.delete()
        return "success"
    except:
        return "error"

@app.route('/update')
def update():
    try:
        connectDB.update()
        return "success"
    except:
        return "error"

if __name__ == "__main__":
    app.run(host="0.0.0.0")