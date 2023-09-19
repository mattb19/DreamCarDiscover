from flask import Flask, request, render_template
from flask_session import Session
import sqlite3
import json
import logging
from werkzeug.security import generate_password_hash, check_password_hash
from flask_modals import Modal
from flask_modals import render_template_modal

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
modal = Modal(app)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'secret!'
Session(app)



def connectDB():
    conn = None
    try:
        conn = sqlite3.connect('TheBank.db')
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        loginname = str(request.form.get("username"))
        loginpassword = str(request.form.get("password"))
        
        conn = connectDB()
        
    return render_template("login.html")
        
        