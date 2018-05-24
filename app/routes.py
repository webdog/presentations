from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='webdog')


@app.route('/presentations')
def hello():
    return render_template('demo.html')


@app.route('/presentations/<slides>')
def presentation(slides):
    html = ''
    presopath = 'app/static/presentations/' + slides
    with open(presopath, 'r') as f:
        html = f.read()
    return render_template('preso.html', html=html)

