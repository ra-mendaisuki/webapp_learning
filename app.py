from flask import Flask

app: Flask = Flask(__name__)


# 「/」にアクセスがあった場合のルーティング
@app.route('/')
def index():
    return "<h1> これは掲示板のトップページです </h1>"


# 「/write」２アクセスが合った場合のルーティング
@app.route("/write")
def write():
    return "<h1> これは掲示板の書き込みページです。 </h1>"

# 「/edit/message_id」にアクセスが合った場合のルーティング
@app.route("/edit/<int:message_id>")
def edit(message_id):
    return f"<h1>これはID={type(message_id).__name__}の編集ページです。</h1>"

if __name__ == "__main__":
    app.run(debug=True)