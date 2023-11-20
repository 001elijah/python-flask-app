import os

from flask import Flask

app = Flask(__name__)

if os.environ["FLASK_ENV"] == "production":
    app.config.from_object("config.Production")
elif os.environ["FLASK_ENV"] == "testing":
    app.config.from_object("config.Testing")
else:
    app.config.from_object("config.Development")

from app import views
from app import admin_views
