#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request, abort
import parser as p
from flask_sqlalchemy import SQLAlchemy
from search.conjugate import get_conjugation

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class verbForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part1 = db.Column(db.String(80), nullable=False)
    part2 = db.Column(db.String(80), nullable=False)
    part3 = db.Column(db.String(80), nullable=False)
    part4 = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'({self.part1}, {self.part2}, {self.part3}, {self.part4})'

    def __list__(self):
        return [str(self.part1), str(self.part2), str(self.part3), str(self.part4)]


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/api', methods=["GET"])
def api():
    if not p.valid(request.args):
        abort(400)
    if "verb" in request.args:
        return str(get_conjugation(request.args["verb"],
                                   request.args["voice"], request.args["tense"]))
    return "Declining Nouns is currently not supported."


@app.route('/tests')
def tests():
    return str(verbForm.query.filter_by(part2="monEre").first())


@app.errorhandler(404)
def handle_404(e):
    return render_template("404.html"), 404


@app.errorhandler(400)
def handle_400(e):
    return render_template("400.html"), 400

def find(s: str):
    return ["vocO", "vocAre", "vocAvI", "vocAtum"]

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    p.start_databases()
    app.run(debug=True)
