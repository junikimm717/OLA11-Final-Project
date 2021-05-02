#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request, abort
import parser as p

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/api', methods=["GET"])
def api():
    if not p.valid(request.args):
        abort(400)
    return str(request.args)

@app.errorhandler(404)
def handle_404(e):
    return render_template("404.html"), 404

@app.errorhandler(400)
def handle_400(e):
    return render_template("400.html"), 400


if __name__ == "__main__":
    app.run(debug=True)
