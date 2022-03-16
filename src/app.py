from flask import Flask



app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>kya kr rahi hai meri jaan</h1>"
#mm

if __name__=="__main__":
    app.run()