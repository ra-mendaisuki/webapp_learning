from flask import Flask, render_template, request

class Message:
    def __init__(self, id:str, user_name:str, contents: str):
        self.id = id
        self.user_name = user_name
        self.contents = contents

# グローバル変数の宣言
app: Flask = Flask(__name__)
login_user_name:str = "osamu"
message_list: list[Message] = [
    Message("202400502102310", "osamu", "朝からビールですか？楽しみですね"),
    Message("202400502102311", "noriko", "こちらこそ！次回はABコースです！"),
    Message("202400502102312", "osamu", "昨日はHBコース楽しかったです。")
]

# 「/」にアクセスがあった場合のルーティング
@app.route('/')
def index():
    # GETメソッドのフォームの値を取得
    search_word: str = request.args.get("search_word")

    # search_word変数の有無を判定
    if search_word is None:
        # すべてのメッセージを「top.html」に表示
        return render_template(
            "top.html",
            login_user_name=login_user_name,
            message_list=message_list
        )
    else:
        # 検索ワードでフィルターしたメッセージを「top.html」に表示
        filtered_message_list: list[Message] = [
            message for message in message_list if search_word in message.contents
        ]
        return render_template(
            "top.html",
            login_user_name=login_user_name,
            message_list=filtered_message_list,
            search_word=search_word
        )

# 「/write」でアクセスがあった場合のルーティング
@app.route("/write", methods=["POST", "GET"])
def write():
    return render_template("write.html")

# 「/edit/message_id」にアクセスが合った場合のルーティング
@app.route("/edit/<int:message_id>")
def edit(message_id):
    return f"<h1>これはID={type(message_id).__name__}の編集ページです。</h1>"

if __name__ == "__main__":
    app.run(debug=True)