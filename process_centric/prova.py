from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from functools import wraps
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *


app = Flask(__name__)


@app.route('/company')
def company():
    return render_template('company.html')





if __name__ == '__main__':
    app.run(port=5070)
