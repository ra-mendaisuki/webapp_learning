from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from pymongo import MongoClient
from pymongo.server_api import ServerApi
# グローバル変数の宣言
app: Flask = Flask(__name__)

socketio = SocketIO(app)

mongo_uri = ""
# Create a new client and connect to the server
client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client["SNS"]
messages_collection = db["messages"]

# 「/」にアクセスがあった場合のルーティング
@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('load messages')
def load_messages():
    messages = messages_collection.find().sort('_id', -1).limit(10)
    messages = list(messages)[::-1]
    messages_return = [message['message'] for message in messages]
    emit('load all messages', messages_return)

@socketio.on('send message')
def send_message(message):
    messages_collection.insert_one({'message': message})
    emit('load one message', message, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
