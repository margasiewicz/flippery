from flask import render_template
from flippers.models import User, Msgs
from flippers import app, db


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")