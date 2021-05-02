#!/usr/bin/env python3

from main import app


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

