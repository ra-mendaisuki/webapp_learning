from flask import Flask, render_template

app: Flask = Flask(__name__)

class Message:
    def __init__(self, id:str, user_name:str, contents: str):
        self.id = id
        self.user_name = user_name
        self.contents = contents

# 「/」にアクセスがあった場合のルーティング
@app.route('/')
def index():
    login_user_name: str = "osamu"

    message_list = [
        Message("202400502102310", "osamu", "朝からビールですか？楽しみですね"),
        Message("202400502102311", "noriko", "こちらこそ！次回はABコースです！"),
        Message("202400502102312", "osamu", "昨日はHBコース楽しかったです。")
    ]
    return render_template(
        "top.html", login_user_name=login_user_name, message_list=message_list
    )


# 「/write」でアクセスがあった場合のルーティング
@app.route("/write")
def write():
    return render_template("write.html")

# 「/edit/message_id」にアクセスが合った場合のルーティング
@app.route("/edit/<int:message_id>")
def edit(message_id):
    return f"<h1>これはID={type(message_id).__name__}の編集ページです。</h1>"

if __name__ == "__main__":
    app.run(debug=True)