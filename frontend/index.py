from flask import Flask, render_template

increasing = False
decreasing = False

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
