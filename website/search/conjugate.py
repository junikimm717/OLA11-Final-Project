#!/usr/bin/env python3

from . import rules

active = {
    "present": [
        ["O", "As", "at", "Amus", "Atis", "ant"],
        ["eO", "Es", "et", "Emus", "Etis", "ent"],
        ["O", "is", "it", "imus", "itis", "unt"],
        ["iO", "Is", "it", "Imus", "Itis", "iunt"],
    ],
    "imperfect": [
        ["Abam", "AbAs", "Abat", "AbAmus", "AbAtis", "Abant"],
        ["Ebam", "EbAs", "Ebat", "EbAmus", "EbAtis", "Ebant"],
        ["Ebam", "EbAs", "Ebat", "EbAmus", "EbAtis", "EbAnt"],
        ["iebam", "iEbAs", "iEbat", "iEbAmus", "iEbAtis", "iEbant"]
    ],
    "future": [
        ["AbO", "Abis", "Abit", "Abimus", "Abitis", "bunt"],
        ["EbO", "Ebis", "bit", "bimus", "bitis", "bunt"],
        ["am", "Es", "et", "Emus", "Etis", "ent"],
        ["iam", "iEs", "iet", "iEmus", "iEtis", "ient"],
    ],
    "perfect": [
        ["I", "istI", "it", "imus", "istis", "erunt"] for _ in range(4)
    ],
    "pluperfect": [
        ["eram", "erAs", "erat", "erAmus", "erAtis", "erant"] for _ in range(4)
    ],
    "future perfect": [
        ["erO", "eris", "erit", "erimus", "eritis", "erint"] for _ in range(4)
    ],
    "infinitive": [
        ["Are", "isse", "Urus esse"],
        ["Ere", "isse", "Urus esse"],
        ["ere", "isse", "Urus esse"],
        ["Ire", "isse", "Urus esse"],
    ],
    "imperative": [
        ['A', 'Ate'],
        ['E', 'Ete'],
        ['e', 'ite'],
        ['I', 'Ite']
    ]
}

passive = {
    "present": [
        ["or", "Aris", "atur", "Amur", "AmInI", "antur"],
        ["eor", "Eris", "etur", "Emur", "EmInI", "entur"],
        ["or", "eris", "itur", "imur", "imInI", "untur"],
        ["ior", "Iris", "Itur", "Imur", "ImInI", "iuntur"],
    ],
    "imperfect": [
        ["Abar", "AbAris", "Abatur", "AbAmur", "AbAmInI", "Abantur"],
        ["Ebar", "EbAris", "Ebatur", "EbAmur", "EbAmInI", "Ebantur"],
        ["Ebar", "EbAris", "Ebatur", "EbAmur", "EbAmInI", "Ebantur"],
        ["iEbar", "iEbAris", "iEbatur", "iEbAmur", "iEbAmInI", "iEbantur"]
    ],
    "future": [
        ["A" + c for c in ["bor", "beris", "bitur", "bimur", "bimInI", "buntur"]],
        ["E" + c for c in ["bor", "beris", "bitur", "bimur", "bimInI", "buntur"]],
        [c for c in ["ar", "Eris", "Etur", "Emur", "EminI", "entur"]],
        ["i" + c for c in ["ar", "Eris", "Etur", "Emur", "EminI", "entur"]],
    ],
    "perfect": [
        ["us sum", "us es", "us est", "I sumus", "I estis", "I sunt"] for _ in range(4)
    ],
    "pluperfect": [
        ["us eram", "us erAs", "us erat", "I erAmus", "I erAtis", "I erant"] for _ in range(4)
    ],
    'future perfect': [
        ["us erO", "us eris", "us erit", "I erimus", "I eritis", "I erunt"] for _ in range(4)
    ],
    "infinitive": [
        ["ArI", "us esse"],
        ["ErI", "us esse"],
        ["I", "us esse"],
        ["IrI", "us esse"],
    ]
}

stems_active = {
    "present": 0,
    "imperfect": 0,
    "future": 0,
    "perfect": 1,
    "pluperfect": 1,
    "future perfect": 1,
    "imperative": 0,
}

stems_passive = {
    "present": 0,
    "imperfect": 0,
    "future": 0,
    "perfect": 2,
    "pluperfect": 2,
    "future perfect": 2,
}


def get_conjugation(verb: str, voice: str, tense: str):
    v = rules.Verb(verb)
    if v.conjugation == 4:
        return None, "irregular"
    if voice == "active":
        if tense in active:
            if tense == "infinitive":
                e = active[tense][v.conjugation]
                return [v.stems[i] + e[i] for i in range(3)]
            return v.add(stems_active[tense], active[tense][v.conjugation])
        return None, tense

    if voice == "passive":
        if tense in passive:
            if tense == "infinitive":
                e = passive[tense][v.conjugation]
                return [v.stems[2*i] + e[i] for i in range(2)]
            return v.add(stems_passive[tense], passive[tense][v.conjugation])
        return None, tense
    return None, "no valid voice"


# run tests

def tests():
    print("test 1...")
    print(get_conjugation("monEre", "active", "present"))
    print(get_conjugation("monEre", "active", "perfect"))
    print(get_conjugation("monEre", "passive", "perfect"))
    print(get_conjugation("monEre", "passive", "perfect"))
    print(get_conjugation("monEre", "active", "infinitive"))
    print(get_conjugation("monEre", "passive", "infinitive"))


if __name__ == "__main__":
    tests()
