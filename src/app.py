from flask import Flask



app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello world 123 798</h1>"
#mmfggmffe     
   
if __name__=="__main__":
    app.run()