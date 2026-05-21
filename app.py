from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    age: int = 19
    return "<h1>あなたの年齢は" + age + "歳です</h1>"


if __name__ == '__main__':
    app.run(debug=True)
