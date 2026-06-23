"""
    :author: tuhd2
    :license: MIT, see LICENSE for more details.
"""
import os
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string tuhd2')

@app.route('/')
def index():
    return render_template('intro.html')

@app.route('/countdown')
def countdown():
    return render_template('countdown.html')

@app.route('/hpbd')
def hpbd():
    return render_template('hpbd.html')

if __name__ == '__main__':
    app.run(debug=True)
