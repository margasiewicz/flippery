from flask import render_template, url_for, flash, redirect, request
from flippers.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

from flippers.models import User, Msgs
from flippers import app, db, bcrypt
import json



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

    
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash('Wrong email or password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


'''
API FROM HERE
'''

@app.route('/addcredit', methods=['POST'])
@login_required
def addcredit():
    '''
    Remember to set Timer: Auto Off in Shelly App
    auth_key: Shelly1 auth_key
    id : Shelly1 id
    '''

    json_data = {
    "auth_key":"<AUTH_KEY here>",
    "id":"<ID here>",
    "channel":"0",
    "turn":"on"
    }

    r1 = requests.post('https://shelly-12-eu.shelly.cloud/device/relay/control',data=json_data)
    return r1.json()


'''
following links are to be hit by Shelly 1's
each time a coin is being recieved
'''
@app.route('/addincome2', methods=['GET'])
def addincome2():  
  new_income = Msgs(message='Test flipper 2zl')

  db.session.add(new_income)
  db.session.commit()

  return json.dumps({'message':'2zl recieved'})

@app.route('/addincome5', methods=['GET'])
def add_product():
  new_income = Msgs(message='Test flipper 5zl')

  db.session.add(new_income)
  db.session.commit()
  return json.dumps({'message':'5zl recieved'})