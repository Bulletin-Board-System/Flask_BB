import dbsql
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    search = request.args.get('search')
    if not search:
        datas = dbsql.data()
    else:
        datas = dbsql.search(search)
    return render_template('main.html', results=datas)

@app.route('/page/<id>')
def page(id):
    datas = dbsql.view(id)
    dbsql.saw(id)
    return render_template('page.html', results=datas)

@app.route('/create', methods=['GET', 'POST'])
def create():
    try:
        if request.method == 'GET':
            return render_template('create.html')
        elif request.method == 'POST':
            title = request.form.get('title')
            creater = request.form.get('creater')
            details = request.form.get('details')
            hide = request.form.get('hide')
            if hide:
                creater = "ㅇㅇ"
            if not title or not details or not creater:
                return "<script>alert('빈칸을 채워주세요'); history.go(-1)</script>"
            dbsql.create(title, creater, details)
            return redirect(url_for('index'))
    except:
        return f"<script>alert('Error: {str(Exception)}'); history.go(-1)</script>"

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    try:
        if request.method == 'GET':
            datas = dbsql.view(id)
            return render_template('update.html', results=datas)
        elif request.method == 'POST':
            ntitle = request.form.get('title')
            details = request.form.get('details')
            if not ntitle or not details:
                return "<script>alert('빈칸을 채워주세요'); history.go(-1)</script>"
            dbsql.update(id, ntitle, details)
            return redirect(url_for('index'))
    except:
        return f"<script>alert('Error: {str(Exception)}'); history.go(-1)</script>"

@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    try:
        dbsql.delete(id)
        return redirect(url_for('index'))
    except:
        return f"<script>alert('Error: {str(Exception)}'); history.go(-1)</script>"
    
app.run(host="0.0.0.0", debug=True, port=8000)