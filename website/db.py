#!/usr/bin/env python3


from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('sqlite:///db.sqlite3', echo=False)

Base = declarative_base()


class verbForm(Base):
    __tablename__ = "verbs"

    id = Column(Integer, primary_key=True)
    part1 = Column(String)
    part2 = Column(String)
    part3 = Column(String)
    part4 = Column(String)

    def __init__(self, part1, part2, part3, part4):
        self.part1 = part1
        self.part2 = part2
        self.part3 = part3
        self.part4 = part4

    def tolist(self):
        return [self.part1, self.part2, self.part3, self.part4]


class nounForm(Base):
    __tablename__ = "nouns"
    id = Column(Integer, primary_key=True)
    nominative = Column(String)
    genitive = Column(String)
    gender = Column(String)
    istem = Column(Boolean)

    def __init__(self, nominative, genitive, gender, istem=False):
        self.nominative = nominative
        self.genitive = genitive
        self.gender = gender
        self.istem = istem

    def tolist(self):
        return [self.nominative, self.genitive, self.gender, self.istem]


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def load_verbs(path: str):
    with open(path, "r") as r:
        lines = r.read().splitlines()
        for line in lines:
            lt = line.split()
            session.add(verbForm(lt[0], lt[1], lt[2], lt[3]))


def load_nouns(path: str):
    with open(path, "r") as r:
        lines = r.read().splitlines()
        for line in lines:
            lt = line.split()
            session.add(nounForm(lt[0], lt[1], lt[2], len(lt) == 4))


def find_verb(verb: str):
    obj = session.query(verbForm).filter_by(part2=verb).first()
    if obj is None:
        return None
    return obj.tolist()


def find_noun(noun: str):
    obj = session.query(nounForm).filter_by(nominative=noun).first()
    if obj is None:
        return None
    return obj.tolist()


def exists(word: str, part):
    if part == 'verb':
        return session.query(verbForm).filter_by(part2=word).first() is not None
    elif part == 'noun':
        return session.query(nounForm).filter_by(nominative=word).first() is not None


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

