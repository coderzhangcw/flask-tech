"""
flask test

pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.register_blueprint
    app.run(debug=True)