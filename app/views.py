from app import app

from flask import render_template, request, redirect

from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return  dt.strftime("%d %b %Y")

@app.route("/")
def hello():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    my_name= "Illia"
    my_gh_nickname= "001elijah"
    age=27
    skills=[ "Python", "HTML5/CSS3/SASS", "Responsive/Adaptive design", "GIT/Parcel/Webpack", "JavaScript", "TypeScript", "Angular", "React/React Native", "Next.js", "Redux", "REST API/CRUD", "Bootstrap", "Node.js", "Nest.js", "MongoDB/SQLite", "Mongoose", "Express", "DatoCMS", "GraphQL API/Apollo", "Markdown" ]
    friends={
        "Tom": 30,
        "Tania": 28,
        "Sasha": 28,
        "Paul": 21
    }
    
    colors=("Red", "Green", "White")

    cool = True

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pulling repo {self.name}"
        
        def clone(self):
            return f"Cloning into {self.url}"
        
    my_remote = GitRemote(
        name="Flask Jinja",
        description="template design tutorial",
        url="https://github.com/001elijah/python-flask-app"
    )
        
    def repeat(x, qty):
        return x * qty
    
    date = datetime.utcnow()

    my_html = "<h1>THIS IS SOME HTML</h1>"

    suspicious = "<script>alert('You got HACKED')</script>"

    return render_template("public/jinja.html",
                           my_name=my_name,
                           my_gh_nickname=my_gh_nickname,
                           age=age,
                           skills=skills,
                           friends=friends,
                           colors=colors,
                           cool=cool,
                           GitRemote=GitRemote,
                           my_remote=my_remote,
                           repeat=repeat,
                           date=date,
                           my_html=my_html,
                           suspicious=suspicious
                           )

@app.route("/about")
def about():
    return "<h1 style='color: red' >About</h1>"

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        req = request.form

        username = req["username"]
        email = req.get("email")
        password = request.form["password"]

        print( username, email, password)

        return redirect(request.url)
    return render_template("public/sign_up.html")

users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creator of the Flask framework",
        "twitter_handle": "@mitsuhiko"
    },
    "gvanrossum": {
        "name": "Guie Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum"
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "A killer of Ukrainians, russian agent, twitter cunt",
        "twitter_handle": "@elonmusk"
    },
}

@app.route("/profile/<username>")
def profile(username):
    user = None
    
    if username in users: 
        user = users[username]
    return render_template("public/profile.html", username=username, user=user)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"
