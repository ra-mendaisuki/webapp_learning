from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# グローバル変数の宣言
app: Flask = Flask(__name__)
login_user_name:str = "osamu"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    contents = db.Column(db.String(100))

# 「/」にアクセスがあった場合のルーティング
@app.route('/')
def index():
    # GETメソッドのフォームの値を取得
    search_word: str = request.args.get("search_word")

    # search_word変数の有無を判定
    if search_word is None:
        message_list: list[Message] = Message.query.all()
    else:
        message_list: list[Message] = Message.query.filter(Message.contents.like(f"%{search_word}%")).all()
    return render_template(
        "top.html",
        login_user_name=login_user_name,
        message_list=message_list,
        search_word=search_word
    )

# 「/write」でアクセスがあった場合のルーティング
@app.route("/write", methods=["POST", "GET"])
def write():
    # GET method
    if request.method == "GET":
        return render_template("write.html", login_user_name=login_user_name)

    # POST method
    elif request.method == "POST":
        contents: str = request.form.get("contents")
        user_name: str = request.form.get("user_name")
        new_message: Message = Message(user_name=user_name, contents=contents)
        db.session.add(new_message)

        db.session.commit()

        return redirect(url_for("index"))

@app.route("/update/<int:message_id>", methods=["POST", "GET"])
def update(message_id:int):
    message: Message = Message.query.get(message_id)
    if request.method == "GET":
        return render_template("update.html", login_user_name=login_user_name, message=message)

    elif request.method == "POST":
        message.contents = request.form.get("contents")
        db.session.commit()

        return redirect(url_for("index"))

@app.route("/delete/<int:message_id>")
def delete(message_id: int):
    message: Message = Message.query.get(message_id)
    db.session.delete(message)
    db.session.commit()

    return redirect(url_for("index"))

# データベースの初期化
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)