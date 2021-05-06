#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request, abort
import parser as p
from search.conjugate import get_conjugation
from search.decline import get_declension
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/api', methods=["GET"])
def api():
    if not p.valid(request.args):
        abort(400)
    if "verb" in request.args:
        if not db.exists(request.args["verb"], 'verb'):
            abort(404)
        return str(get_conjugation(request.args["verb"],
                                   request.args["voice"], request.args["tense"]))
    else:
        if not db.exists(request.args["noun"], 'noun'):
            abort(404)
        return str(get_declension(request.args["noun"]))


@app.route('/tests')
def tests():
    return str()


@app.errorhandler(404)
def handle_404(e):
    return render_template("404.html"), 404


@app.errorhandler(400)
def handle_400(e):
    return render_template("400.html"), 400


def find(s: str):
    return ["vocO", "vocAre", "vocAvI", "vocAtum"]


if __name__ == "__main__":
    app.run(debug=True)
