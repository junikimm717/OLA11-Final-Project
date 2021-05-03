#!/usr/bin/env python3

from db import find_verb

def detect_conjugation(verb: str) -> int:
    vowel = verb[-3]
    if vowel == "A":
        return 0
    elif vowel == "E":
        return 1
    elif vowel == "e":
        return 2
    elif vowel == "I":
        return 3
    return 4


def get_stems(lt: list) -> list:
    return [lt[1][:-3], lt[2][:-1], lt[3][:-2]]


class Verb:
    def __init__(self, verb: str):
        self.stems = get_stems(find_verb(verb))
        self.conjugation = detect_conjugation(verb)

    def add(self, stem: int, endings: list):
        return [self.stems[stem] + endings[i] for i in range(len(endings))]
