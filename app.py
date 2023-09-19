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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        registername = str(request.form.get("username"))
        print(registername)
        registerpassword = str(request.form.get("password"))
        registerpassword = generate_password_hash(registerpassword)
        registeremail = str(request.form.get("email"))
        conn = connectDB()
        id = int(str(conn.execute("SELECT COUNT(*) FROM User").fetchall()[0]).strip('(').strip(')').strip(','))+1
        conn.execute("INSERT INTO User VALUES (0, ?, ?, ?, ?, 0)", (registeremail, id, registerpassword, registername))
        conn.commit()
        return "SUCCESS"
    else:
        return render_template("login.html")
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        print("dwdwdw")
        loginname = str(request.form.get("username"))
        loginpassword = str(request.form.get("password"))
        
        conn = connectDB()
        user = str(conn.execute("SELECT Name FROM User WHERE Name=?", (loginname,)).fetchall()).strip('(').strip(')').strip(',')
        password = str(conn.execute("SELECT Password FROM User WHERE Name=?", (loginname,)).fetchall()).strip('(').strip(')').strip(',')
        
        
        password = list(password)
        newp = ""
        for i in password:
            if i.isalnum() or i in ['!', '%', '$', '#', ':']:
                newp += i
        
        user= list(user)
        newu = ""
        for i in user:
            if i.isalnum() or i in ['!', '%', '$', '#']:
                newu += i
        
        if newu==loginname and check_password_hash(newp, loginpassword)==True:
            return "SUCCESS"
        else:
            return "User Not Found"
    else:
        return render_template("login.html")
    
def connectDB():
    conn = None
    try:
        conn = sqlite3.connect('TheBank.db')
    except sqlite3.Error as e:
        print(e)
    return conn