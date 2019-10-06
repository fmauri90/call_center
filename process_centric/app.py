from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from functools import wraps
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import requests, json
engine = create_engine('sqlite:///call_center.db', echo=True)

app = Flask(__name__)

app.secret_key = "my precious"

BUSINESS_LOGIC_HOST = 'http://127.0.0.1:5080'

# login required decorator


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first!')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@login_required
def home():
    ### lista company
    #### - endpoint interno al servizio
    return render_template('index.html')

@app.route('/company/<company_id>')
@login_required
def view_company_condominium(company_id):
    condominium_company_bus = requests.get('{}/{}/condominium'.format(BUSINESS_LOGIC_HOST, company_id),
                                           headers={"Content-Type": "application/json"})
    data = json.loads(condominium_company_bus.text)
    print(data)
    if 'items' in data:
        return render_template('company_information.html', items=data['items'])
    else:
        return error


@app.route('/<company_id>/technical')
@login_required
def view_company_technicians(company_id):
    technical_company = requests.get('{}/{}/technical'.format(BUSINESS_LOGIC_HOST, company_id),
                                     headers={"Content-Type": "application/json"})
    data = json.loads(technical_company.text)
    print(data)
    if 'items' in data:
        return render_template('technician_information.html', items=data['items'])
    else:
        return error


@app.route('/companies')
@login_required
def view_companies():
    technical_company = requests.get('{}/companies'.format(BUSINESS_LOGIC_HOST),
                                     headers={"Content-Type": "application/json"})
    data = json.loads(technical_company.text)
    print(data)
    if 'items' in data:
        return render_template('company.html', items=data['items'])
    else:
        return error



@app.route('/call/{}')
@login_required
def view_calls_day():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        post_name = str(request.form['username'])
        post_password = str(request.form['password'])

        Session = sessionmaker()
        Session.configure(bind=engine)
        s = Session()
        query_login = s.query(User).filter(User.username.in_([post_name]), User.password.in_([post_password]))
        result = query_login.first()
        if result:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again!')
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('welcome'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
