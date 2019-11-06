#!flask/bin/python
import os
import sys

from flask import (Flask, abort, jsonify, render_template, redirect, url_for, 
                    make_response, request)
from forms.form_login import LoginForm
from forms.form_signup import SignupForm
from config import Config

app = Flask(__name__, static_url_path = "")
app.config.from_object(Config)

@app.errorhandler(400)
def bad_request(error):
    return '''<div>400</div>'''

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( {'error': 'Not found'} ), 404)

@app.errorhandler(405)
def not_allowed(error):
    return make_response(jsonify( {'error': 'Not allowed' } ), 405)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate():
            return redirect(url_for('index'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/index')
def index():
    return '''
<html>
    <head>
        <title>Index</title>
    </head>
    <body>
        <ul>
            <li>a</li>
            <li>b</li>
            <li>c</li>
        </ul>
    </body>
</html>'''

if __name__ == '__main__':
    app.run(debug = True)

