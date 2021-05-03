from .rules import noun

declensions = {
    "0": ["ae", "ae", "am", "A", "ae", "Arum", "Is", "As", "Is"],
    "1": ["I", "O", "um", "O", "I", "Orum", "Is", "Os", "Is"],
    "1n": ["I", "O", "", "O", "I", "Orum", "Is", "Os", "Is"],
    "2": ["is", "I", "em", "e", "Es", "um", "ibus", "Es", "ibus"],
    "2i": ["is", "I", "em", "e", "Es", "ium", "ibus", "Es", "ibus"],
    "2n": ["is", "I", "", "e", "a", "um", "ibus", "a", "ibus"],
    "2ni": ["is", "I", "", "I", "ia", "ium", "ibus", "ia", "ibus"],
    "3": ["Us", "uI", "um", "U", "Us", "uum", "ibus", "Us", "ibus"],
    "3n": ["Us", "U", "", "U", "ua", "uum", "ibus", "ua", "ibus"],
    "4": ["eI", "eI", "em", "E", "Es", "Erum", "Ebus", "Es", "Ebus"],
}

stems = {
    "m": [1, 1, 1, 1, 1, 1, 1, 1, 1],
    "f": [1, 1, 1, 1, 1, 1, 1, 1, 1],
    "n": [1, 1, 0, 1, 1, 1, 1, 1, 1],
}


def get_declension(nominative: str):
    n: noun.Noun = noun.Noun(nominative)
    if n.declension is None:
        return None, f'{nominative} has not been found in the database.'
    query = str(n.declension.declension)
    if n.declension.gender == 'n': query += 'n'
    if n.declension.istem and n.declension.declension == 3: query += 'i'
    endings = declensions[query]
    s = [n.stem[stems[n.declension.gender][i]] for i in range(9)]
    return str([n.stem[0]] + [s[i] + endings[i] for i in range(9)])
