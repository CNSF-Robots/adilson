from flask import Flask
from flask_cors import CORS

import bot as b

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    response = {
        "api":"Adilson Chatbot",
        "version":"v001"
    }
    return response 

@app.route('/chat_flow/<text>', methods=['GET'])
def chat_flow(text:str):
    return b.chat(text)

if __name__ == '__main__':
   app.run(debug=True)