# import requests
# import os 
# from dotenv import load_dotenv
# api_key=os.getenv("hf_api_key")
# if not api_key:
#     print("API key not found")
# headers='{"authorization":f"bearer {api_key}}'
# url="https://huggingface.co/openai-community/gpt2"
# payload={"inputs":"give me a quotation on success"}
# data=requests.post(url,headers=headers,json=payload)
# result=data.json()
# print(result)

import requests
import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, render_template,request
# from flask_mysqldb import MySQL

load_dotenv()

API_KEY = os.getenv("NINJA_API_KEY")

con=mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_DATABASE")
    )
cursor=con.cursor()

if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

API_URL = "https://api.api-ninjas.com/v1/quotes"

headers = {
    "X-Api-Key": API_KEY
}

app = Flask(__name__)

def generate_ai_quote():
    response = requests.get(API_URL, headers=headers)
    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        quote = data[0]["quote"]
        author = data[0]["author"]
        return quote, author
    else:
        return "No quote received", "Unknown"

@app.route("/ai")
def index():
    quote, author = generate_ai_quote()
    return render_template(
        "index.html",
        quote=quote,
        author=author
    )

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/registration',methods=['GET','POST'])
def registration():
    if request.method=="POST":
        user=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        cursor.execute("insert into registration (username,email,password) values (%s,%s,%s)",[user,email,password])
        con.commit()
        return "values stored"
    return render_template('registration.html')

from flask import render_template, request, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM login WHERE username=%s AND password=%s",
            (user, password)
        )
        result = cursor.fetchone()

        if result:
            # redirect to AI Quote Generator page
            return redirect(url_for('home'))
        else:
            return "Invalid username or password"

    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)

# from flask import Flask,render_template
# app = Flask(__name__)

# @app.route('/home')
# def home():
#     return "python"

# @app.route('/index')
# def index_html():
#     return render_template('index.html')

# app.run(use_reloader=True)
