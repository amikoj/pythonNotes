#!/usr/bin/env python
# -*-encoding:utf-8-*-

from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())


@app.route('/form',methods = ['GET','POST'])
def formFunc():
    form = NameForm()
    if form.validate_on_submit():
        session['name' ] = form.name.data
        return redirect(url_for('formFunc'))
    return render_template('form.html',form=form,name=session.get('name'))

app.run(debug=True)