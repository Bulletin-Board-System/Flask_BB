from flask import Flask, render_template, request
import connectDB

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/create')
def create():
    try:
        connectDB.create('create')
        return "success"
    except:
        return "error"

@app.route('/login')
def login():
    try:
        connectDB.login
    except:
        return "error"

@app.route('/sign')
def sign():
    try:
        uname = request.form['uname']
        password = request.form['password']
        connectDB.sign(uname, password)
        return "success"
    except:
        return "error"

@app.route('/delete')
def delete():
    try:
        connectDB.delete('delete')
        return "success"
    except:
        return "error"

@app.route('/update')
def update():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")