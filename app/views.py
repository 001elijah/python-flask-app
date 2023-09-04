from app import app

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/about")
def about():
    return "<h1 style='color: red' >About</h1>"