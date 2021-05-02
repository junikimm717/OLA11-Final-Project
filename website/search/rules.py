#!/usr/bin/env python3

from enum import Enum
from .finder import find

class Conjugation(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    IRREGULAR = 5

def detect_conjugation(verb: str) -> Conjugation:
    vowel = verb[-3]
    if vowel == "A":
        return Conjugation.FIRST
    elif vowel == "E":
        return Conjugation.SECOND
    elif vowel == "e":
        return Conjugation.THIRD
    elif vowel == "I":
        return Conjugation.FOURTH
    return Conjugation.IRREGULAR

def get_stems(l: list) -> list:
    return [l[1][:-3], l[2][:-1], l[3][:-2]]

class Verb:
    def __init__(self, verb: str):
        self.stems = get_stems(find(verb))
        self.conjugation = detect_conjugation(verb)

    def add(self, stem:int, endings: list):
        return [self.stems[stem] + endings[i] for i in range(len(endings))]


active = [
    [
        ["O", "As", "at", "Amus", "Atis", "ant"]
        ["O", "Es", "et", "Emus", "Etis", "ent"]
        ["O", "is", "it", "imus", "itis", "unt"]
        ["O", "Is", "it", "Imus", "Itis", "iunt"]
    ],
    [
        ["bAm", "bAs", "bAt", "bAmus", "bAtis", "bAnt"]
        ["EbAm", "EbAs", "EbAt", "EbAmus", "EbAtis", "EbAnt"]
        ["EbAm", "EbAs", "EbAt", "EbAmus", "EbAtis", "EbAnt"]
        ["iebAm", "iebAs", "iebAt", "iebAmus", "iebAtis", "iebAnt"]
    ],
]
