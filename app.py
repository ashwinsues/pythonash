from flask import Flask
app=Flask("__name__")
@app.route("/")
def index():
    return "welcome to my website"
@app.route("/home")
def home():
    return "welcome to the home page"
if(__name__=="__main__"):
    app.run()
   