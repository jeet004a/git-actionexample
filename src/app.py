from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! meri jaan kider"


if __name__=="__main__":
    app.run()