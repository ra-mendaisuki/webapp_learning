from datetime import datetime
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from pymongo import MongoClient

# グローバル変数の宣言
app: Flask = Flask(__name__)

socketio = SocketIO(app)

mongo_uri = "mongodb+srv://dbUser:dbUserPassword@cluster0.6xnpzdi.mongodb.net/"
client = MongoClient(mongo_uri)
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