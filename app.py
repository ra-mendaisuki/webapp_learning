from flask import Flask, render_template

app: Flask = Flask(__name__)


# 「/」にアクセスがあった場合のルーティング
@app.route('/')
def index():
    login_user_name: str = "osamu"
    return render_template("top.html", login_user_name=login_user_name)


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