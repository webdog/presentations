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
        template_definition = f.readline()
        if '!--' in template_definition:
            # This a total hack, will fix later - webdog
            # Custom presentation theme defined in first line of static presentation file
            theme = template_definition.split(': ')[1].replace(' -->', '')
            html = f.read()
            return render_template('preso.html', html=html, theme=theme)
        else:
            html = f.read()
            return render_template('preso.html', html=html)
