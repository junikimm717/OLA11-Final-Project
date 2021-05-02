#!/usr/bin/env python3

import rules

active = [
    [
        ["O", "As", "at", "Amus", "Atis", "ant"],
        ["O", "Es", "et", "Emus", "Etis", "ent"],
        ["O", "is", "it", "imus", "itis", "unt"],
        ["O", "Is", "it", "Imus", "Itis", "iunt"],
    ],
    [
        ["Abam", "AbAs", "Abat", "AbAmus", "AbAtis", "Abant"],
        ["Ebam", "EbAs", "Ebat", "EbAmus", "EbAtis", "Ebant"],
        ["Ebam", "EbAs", "Ebat", "EbAmus", "EbAtis", "EbAnt"],
        ["iebam", "iEbAs", "iEbat", "iEbAmus", "iEbAtis", "iEbant"]
    ],
    [
        ["AbO", "Abis", "Abit", "Abimus", "Abitis", "bunt"],
        ["EbO", "Ebis", "bit", "bimus", "bitis", "bunt"],
        ["am", "Es", "et", "Emus", "Etis", "ent"],
        ["iam", "iEs", "iet", "iEmus", "iEtis", "ient"],
    ],
    [
        ["I", "istI", "it", "imus", "istis", "erunt"] for _ in range(4)
    ],
    [
        ["eram", "erAs", "erat", "erAmus", "erAtis", "erant"] for _ in range(4)
    ],
    [
        ["erO", "eris", "erit", "erimus", "eritis", "erint"] for _ in range(4)
    ],
    [
        ["Are", "isse", "Urus esse"],
        ["Ere", "isse", "Urus esse"],
        ["ere", "isse", "Urus esse"],
        ["Ire", "isse", "Urus esse"],
    ],
    [
        ['A', 'Ate'],
        ['E', 'Ete'],
        ['e', 'ite'],
        ['I', 'Ite']
    ]
]

passive = [
    [
        ["or", "Aris", "atur", "Amur", "AmInI", "antur"],
        ["eor", "Eris", "etur", "Emur", "EmInI", "entur"],
        ["or", "eris", "itur", "imur", "imInI", "untur"],
        ["ior", "Iris", "Itur", "Imur", "ImInI", "iuntur"],
    ],
    [
        ["Abar", "AbAris", "Abatur", "AbAmur", "AbAmInI", "Abantur"],
        ["Ebar", "EbAris", "Ebatur", "EbAmur", "EbAmInI", "Ebantur"],
        ["Ebar", "Eb]ris", "Ebatur", "EbAmur", "EbAmInI", "Ebantur"],
        ["iEbar", "iEbAris", "iEbatur", "iEbAmur", "iEbAmInI", "iEbantur"]
    ],
    [
        ["A" + c for c in ["bor", "beris", "bitur", "bimur", "bimInI", "buntur"]],
        [ "E" + c for c in ["bor", "beris", "bitur", "bimur", "bimInI", "buntur"]],
        [ c for c in ["ar", "Eris", "Etur", "Emur", "EminI", "entur"]],
        [ "i" + c for c in ["ar", "Eris", "Etur", "Emur", "EminI", "entur"]],
    ],
    [
        ["us sum", "us es", "us est", "I sumus", "I estis", "I sunt"] for _ in range(4)
    ],
    [
        ["us eram", "us erAs", "us erat", "I erAmus", "I erAtis", "I erant"] for _ in range(4)
    ],
    [
        ["us erO", "us eris", "us erit", "I erimus", "I eritis", "I erunt"] for _ in range(4)
    ],
    [
        ["ArI", "us esse"],
        ["ErI", "us esse"],
        ["I", "us esse"],
        ["IrI", "us esse"],
    ]
]

def get_ending(verb: str, voice: str, tense: str):
    v = Verb(verb)
    if tense == "imperative":
        if voice == "active":
            
            pass
    
