from flask import Flask,render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import jinja2

app=Flask(__name__)
Bootstrap(app)
app.secret_key = "some secret string"
class myform(FlaskForm):
    email=StringField(name='Email',validators=[DataRequired()])
    password=PasswordField(name='password',validators=[DataRequired()])
    submit=SubmitField(label='login')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    form=myform()
    if form.validate_on_submit():
        # Do something with the form data here
        if form.email.data=='admin@email.com' and form.password.data=='12345678':
             return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html',form=form)





if __name__=='__main__':
    app.run(debug=True)