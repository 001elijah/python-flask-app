import os

from app import app


from flask import render_template, request, redirect, jsonify, make_response

from datetime import datetime

from werkzeug.utils import secure_filename

from flask import send_from_directory, abort


@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")


@app.route("/")
def hello():
    print(f"Flask ENV is set to: {os.environ['FLASK_ENV']}")
    print(f"Current Flask ENV is: {app.config['DB_NAME']}")
    return render_template("public/index.html")


@app.route("/jinja")
def jinja():
    my_name = "Illia"
    my_gh_nickname = "001elijah"
    age = 27
    skills = [
        "Python",
        "HTML5/CSS3/SASS",
        "Responsive/Adaptive design",
        "GIT/Parcel/Webpack",
        "JavaScript",
        "TypeScript",
        "Angular",
        "React/React Native",
        "Next.js",
        "Redux",
        "REST API/CRUD",
        "Bootstrap",
        "Node.js",
        "Nest.js",
        "MongoDB/SQLite",
        "Mongoose",
        "Express",
        "DatoCMS",
        "GraphQL API/Apollo",
        "Markdown",
    ]
    friends = {"Tom": 30, "Tania": 28, "Sasha": 28, "Paul": 21}

    colors = ("Red", "Green", "White")

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
        url="https://github.com/001elijah/python-flask-app",
    )

    def repeat(x, qty):
        return x * qty

    date = datetime.utcnow()

    my_html = "<h1>THIS IS SOME HTML</h1>"

    suspicious = "<script>alert('You got HACKED')</script>"

    return render_template(
        "public/jinja.html",
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
        suspicious=suspicious,
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

        print(username, email, password)

        return redirect(request.url)
    return render_template("public/sign_up.html")


users = {
    "mitsuhiko": {
        "name": "Armin Ronacher",
        "bio": "Creator of the Flask framework",
        "twitter_handle": "@mitsuhiko",
    },
    "gvanrossum": {
        "name": "Guie Van Rossum",
        "bio": "Creator of the Python programming language",
        "twitter_handle": "@gvanrossum",
    },
    "elonmusk": {
        "name": "Elon Musk",
        "bio": "A killer of Ukrainians, russian agent, twitter cunt",
        "twitter_handle": "@elonmusk",
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


@app.route("/json", methods=["POST"])
def json():
    if request.is_json:
        req = request.get_json()

        print(type(req))
        print(req)

        response = {"message": "JSON received!", "name": req.get("name")}

        res = make_response(jsonify(response), 200)

        return res

    else:
        res = make_response(jsonify({"message": "No JSON received!"}), 400)

        return res


@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")


@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    req = request.get_json()

    print(req)

    res = make_response(jsonify({"message": "JSON received"}), 200)

    return res


@app.route("/query")
def query():
    if request.args:
        args = request.args
        for k, v in args.items():
            print(f"{k}: {v}")

        if "foo" in args:
            foo = args.get("foo")
            print(foo)

            args = request.args

            if "title" in args:
                title = request.args.get("title")
                print(title)

                serialized = ", ".join(f"{k}: {v}" for k, v in args.items())
                print(serialized)
        return f"(Query) {serialized}", 200

    else:
        return "Query not received", 400


def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False


def allowed_image(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            if not allowed_image_filesize(request.cookies.get("filesize")):
                print("Maximum filesize exceeded")
                return redirect(request.url)

            image = request.files["image"]

            if image.filename == "":
                print("Must have a file name")
                return redirect(request.url)

            if not allowed_image(image.filename):
                print("That image extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            print("Image saved")

            return redirect(request.url)
        res = make_response(jsonify({"message": "Image saved"}), 200)
        res.set_cookie("same-site-cookie", "foo", samesite="None")
    return render_template("public/upload-image.html")


"""
//converters//
string:
int:
float:
path:
uuid:
"""


@app.route("/get-image/<image_name>")
def get_image(image_name):
    try:
        return send_from_directory(
            directory=app.config["CLIENT_IMAGES"], path=image_name, as_attachment=False
        )
    except FileNotFoundError:
        abort(404)


@app.route("/get-csv/<csv_name>")
def get_csv(csv_name):
    try:
        return send_from_directory(
            directory=app.config["CLIENT_CSV"], path=csv_name, as_attachment=False
        )
    except FileNotFoundError:
        abort(404)


@app.route("/get-pdf/<pdf_name>")
def get_pdf(pdf_name):
    try:
        return send_from_directory(
            directory=app.config["CLIENT_PDF"], path=pdf_name, as_attachment=False
        )
    except FileNotFoundError:
        abort(404)


@app.route("/get-report/<path:filepath>")
def get_pdf(filepath):
    try:
        return send_from_directory(
            directory=app.config["CLIENT_REPORTS"], path=filepath, as_attachment=True
        )
    except FileNotFoundError:
        abort(404)
        
