from flask import Flask
from flask import render_template, url_for, flash, redirect, request, abort

env = 'pro'

app = Flask(__name__)

if env == 'dev': 
    app.debug= True
else:
    app.debug= False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/proj-scol')
def proj__scol():
    return render_template('projets-scolaires.html')

@app.route('/proj-pers')
def proj_pers():
    return render_template('projets-personnels.html')