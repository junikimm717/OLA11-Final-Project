from db import find_noun
from dataclasses import dataclass


@dataclass(order=True, frozen=True)
class Declension:
    declension: int
    gender: str
    istem: bool


def detect_declension(noun: str):
    lt = find_noun(noun)
    if lt is None:
        return None, None
    declension = 5
    stem = ""
    if lt[1].endswith("ae"):
        declension = 0
        stem = lt[1][:-2]
    elif lt[1].endswith("I"):
        declension = 1
        stem = lt[1][:-1]
    elif lt[1].endswith("is"):
        declension = 2
        stem = lt[1][:-2]
    elif lt[1].endswith("Us"):
        declension = 3
        stem = lt[1][:-2]
    elif lt[1].endswith("eI"):
        declension = 4
        stem = lt[1][:-2]

    return Declension(declension, lt[2], lt[3]), [noun, stem]


class Noun:
    def __init__(self, nominative: str):
        self.declension, self.stem = detect_declension(nominative)