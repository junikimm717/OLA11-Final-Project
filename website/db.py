#!/usr/bin/env python3


from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def load_verbs(path: str):
    with open(path, "r") as r:
        lines = r.read().splitlines()
        for line in lines:
            lt = line.split()
            session.add(verbForm(lt[0], lt[1], lt[2], lt[3]))

def find_verb(verb: str):
    obj = session.query(verbForm).filter_by(part2=verb).first()
    if obj is None:
        return None
    return obj.tolist()

def exists(verb: str):
    return session.query(verbForm).filter_by(part2=verb).first() is not None

load_verbs("../pkg/tests/verbs.txt")