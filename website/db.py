#!/usr/bin/env python3


from pymongo import MongoClient
from dataclasses import dataclass
import os

client = MongoClient('localhost', 27017)
verbdb = client['verbs'].verbs
noundb = client['nouns'].nouns

verbdb.drop()
noundb.drop()

@dataclass
class verbForm:
    part1: str
    part2: str
    part3: str
    part4: str

    def todict(self):
        return {"part1": self.part1,
                "part2": self.part2,
                "part3": self.part3,
                "part4": self.part4}

    def tolist(self):
        return [self.part1, self.part2, self.part3, self.part4]


@dataclass
class nounForm:
    nominative: str
    genitive: str
    gender: str
    istem: bool
    
    def todict(self):
        return {"nominative": self.nominative,
                "genitive": self.genitive,
                "gender": self.gender,
                "istem": self.istem}

    def tolist(self):
        return [self.nominative, self.genitive, self.gender, self.istem]


def load_verbs(path: str):
    with open(path, "r") as r:
        lines = r.read().splitlines()
        for line in lines:
            lt = line.split()
            verbdb.insert_one(verbForm(lt[0], lt[1], lt[2], lt[3]).todict())


def load_nouns(path: str):
    with open(path, "r") as r:
        lines = r.read().splitlines()
        for line in lines:
            lt = line.split()
            print(lt)
            noundb.insert_one(nounForm(lt[0], lt[1], lt[2], len(lt) == 4).todict())


def find_verb(verb: str):
    obj = verbdb.find_one({"part2": verb})
    if obj is None:
        return None
    obj = verbForm(obj["part1"], obj['part2'], obj['part3'], obj['part4'])
    return obj.tolist()


def find_noun(noun: str):
    obj = noundb.find_one({"nominative": noun})
    if obj is None:
        return None
    obj = nounForm(obj["nominative"], obj['genitive'], obj['gender'], obj['istem'])
    return obj.tolist()


def exists(word: str, part):
    if part == 'verb':
        return find_verb( word ) is not None
    elif part == 'noun':
        return find_noun( word ) is not None


directory = os.path.dirname(os.path.realpath(__file__))
try:
    path = os.path.join(directory,"../words/verbs")
    for f in os.listdir(path):
        load_verbs(os.path.join(path, f))
except FileNotFoundError:
    pass

try:
    path = os.path.join(directory,"../words/nouns")
    for f in os.listdir(path):
        load_nouns(os.path.join(path, f))
except FileNotFoundError:
    pass

