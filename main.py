from echo import echo, MORSE, ALPHABET

S = 'The quick brown fox jumps over the lazy dogs'

print(echo(S))
print()
print()
print(echo(echo(S)))
print()
print()
print(echo(echo('Hi')))

EQUIVALENT_PROSIGNS = []

for a1 in range(26):
    for a2 in range(26):
        for b1 in range(26):
            for b2 in range(26):
                if a1 == b1 and a2 == b2:
                    continue
                prosign_1 = MORSE[a1] + MORSE[a2]
                prosign_2 = MORSE[b1] + MORSE[b2]
                if prosign_1 == prosign_2:
                    text1 = ALPHABET[a1] + ALPHABET[a2]
                    text2 = ALPHABET[b1] + ALPHABET[b2]
                    EQUIVALENT_PROSIGNS.append(text1 + " = " + text2)

print(EQUIVALENT_PROSIGNS)
print()

print(len(EQUIVALENT_PROSIGNS), "equivalent prosigns in list above")
N_TWO_LETTER = len(ALPHABET) ** 2
print(N_TWO_LETTER, "two-letter prosigns")
N_EDGES = N_TWO_LETTER * (N_TWO_LETTER - 1) / 2
print(N_EDGES, "edges in complete graph")
print(len(EQUIVALENT_PROSIGNS) / 2, "equiv. prosigns, excluding dups")
PROPORTION = len(EQUIVALENT_PROSIGNS) / 2 / N_EDGES
print(PROPORTION, "proportion of edges are equivalent")
