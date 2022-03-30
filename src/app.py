from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>this is chat boot here jack2</h1>"


@app.route("/jeet")
def index1():
    return "<h1>this is nikhil boot here </h1>"


@app.route("/iko")
def index3():
    return "<h1>this is nikhil boot here </h1>"


# mmfggmffefg

if __name__ == "__main__":
    app.run()
