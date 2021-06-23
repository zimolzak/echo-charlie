from echo import MORSE, ALPHABET

SL = ["...---..."]
UL = ['.-..-...-.']


def morse_to_char(morse_string):
    for i in range(len(MORSE)):
        if MORSE[i] == morse_string:
            return ALPHABET[i]
    raise ValueError


def expand_once(morse_list):
    new_list = []
    for r in morse_list:
        if '-' in r and '.' in r:
            first = min(r.find('.'), r.find('-'))
        elif '-' in r:
            first = r.find('-')
        elif '.' in r:
            first = r.find('.')
        else:  # Must be all letters, so keep str w/o expansion
            new_list.append(r)
            continue
        leading_letters = r[0:first]
        trailing_morse = r[first:]
        for n_dits in range(1, 5):
            morse_char = trailing_morse[0:n_dits]
            morse_tail = trailing_morse[n_dits:]
            try:
                my_char = morse_to_char(morse_char)
            except ValueError:  # letter not found like .-.- so do not add anything
                continue
            new_list.append(leading_letters + my_char + morse_tail)
    return new_list


def full_expand(x):
    for i in range(len(x[0])):
        x = expand_once(x)
        if '-' not in x[0] and '.' not in x[0]:
            return set(x)


if __name__ == '__main__':
    s = full_expand(SL)
    print(s)
    print(len(s))
    print()
    print()
    s = full_expand(UL)
    print(s)
    print(len(s))
