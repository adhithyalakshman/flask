from flask import Flask,render_template,request
from datetime import datetime
import requests
import smtplib
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
from wtforms import validators
app=Flask(__name__)
app.secret_key="dummy"
bootstrap=Bootstrap5(app)

class myform(FlaskForm):
    name=StringField('email',validators=[DataRequired()])
    password=PasswordField(label='password' ,validators=[DataRequired()])
    submit=SubmitField(label='go')
@app.route("/")
def home():
    return render_template("/welcome.html")


@app.route("/signin",methods=["POST"])
def login():
    form=myform()

    if form.validate_on_submit():
        if form.name.data=="dummy":
            return render_template("submit.html")
        else:
            return "<h1>refused</h1>"




    return render_template('index.html',form=form)




app.run(debug=True)
