from flask import render_template
from helpers.svg import SVG
from app import app
import os

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
    oct_path = os.listdir('app/static/octicons/svg')
    octicons = {}
    for o in oct_path:
        path = f'app/static/octicons/svg/{o}'
        with open(path, 'r') as f:
            #jinja does not support dashes in variables. change to dash to reference octicons
            key = o.split('.')[0].replace('-', '_')
            octicons[key] = f.readline()

    footer_logo = SVG(octicons['mark_github'])
    footer_logo  = footer_logo.resize(48, 48)



    with open(presopath, 'r') as f:
        template_definition = f.readline()
        if '!--' in template_definition:
            # This a total hack, will fix later - webdog
            # Custom presentation theme defined in first line of static presentation file
            theme = template_definition.split(': ')[1].replace(' -->', '')
            html = f.read()
            return render_template('preso.html', html=html, theme=theme, octicons=octicons, footer_logo=footer_logo)
        else:
            html = f.read()
            return render_template('preso.html', html=html, octicons=octicons)
