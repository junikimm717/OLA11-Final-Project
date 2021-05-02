#!/usr/bin/env python3

from main import db, app, verbForm


def valid(args):
    if "verb" in args:
        if args["verb"] == "":
            return False
        required = ["tense", "voice"]
        for r in required:
            if r not in args or len(args[r]) == 0 or args[r] == None:
                return False
        return True
    if "noun" in args:
        return args["noun"] != ""
    return False


def start_databases():
    test_begin("../pkg/tests/verbs.txt")


def test_begin(file_name):
    with open(file_name, "r") as r:
        i = 0
        for line in r.read().splitlines():
            parts = line.split()
            part1 = parts[0]
            part2 = parts[1]
            part3 = parts[2]
            part4 = parts[3]
            i += 1
            db.session.add(verbForm(id=i, part1=part1, part2=part2, part3=part3, part4=part4))
    db.session.commit()
