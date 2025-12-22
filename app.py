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
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

API_KEY = os.getenv("NINJA_API_KEY")

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

@app.route("/")
def home():
    quote, author = generate_ai_quote()
    return render_template(
        "index.html",
        quote=quote,
        author=author
    )

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