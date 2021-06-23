from treelib import Tree
from echo import MORSE, ALPHABET

S = "...---..."
T = Tree()
T.create_node("_")  # root
UL = ['.-..-...-.']


def morse_to_char(morse_string):
    for i in range(len(MORSE)):
        if MORSE[i] == morse_string:
            return ALPHABET[i]
    raise ValueError


def pop_all_possibilities(morse, tree):
    for n_dits in range(1, 5):
        morse_char = morse[0:n_dits]
        morse_tail = morse[n_dits:]
        try:
            my_char = morse_to_char(morse_char)
            tree.create_node(my_char)
        except ValueError:
            pass
    return morse_tail, tree


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


if __name__ == '__main__':
    for i in range(len(UL[0])):
        UL = expand_once(UL)
        if '-' not in UL[0] and '.' not in UL[0]:
            print(UL)
            break
