from flask import Flask
from flask import render_template, url_for
from secret_key import SECRET_KEY


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)