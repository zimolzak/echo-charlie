PHONETIC_LIST = "alfa bravo charlie delta echo foxtrot golf hotel india juliet kilo lima mike november oscar papa quebec romeo sierra tango uniform victor whiskey xray yankee zulu".split()

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
         "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
         "--.-", ".-.", "...", "-", "..-", "...-",
         ".--", "-..-", "-.--", "--.."]


def echo(input_string):
    """Replace all letters in a string with their phonetic alphabet
    words.
    """
    input_string = input_string.lower()
    output_string = ""
    for char in input_string:  # so we don't .replace() more than once
        for phonetic in PHONETIC_LIST:
            if char == phonetic[0]:
                output_string += phonetic + ' '
        if char == ' ':
            output_string += ', '
        elif char not in ALPHABET:
            output_string += char
    # Tidy up.
    output_string = output_string.replace(' ,', ',')  # No sp before comma
    output_string = output_string.replace(',,', ';')
    output_string = output_string.capitalize()
    return output_string


def morse_to_char(morse_string):
    for i in range(len(MORSE)):
        if MORSE[i] == morse_string:
            return ALPHABET[i]
    raise ValueError


def expand_once(morse_list):
    """Take a list of part-Morse, part-letter strings, and expand each element to at most 4 possible
    Morse interpretations. Works from the start of the string, replacing only one letter.

    Example: r...- maps to re..- ri.- rs- rv
    """
    new_list = []
    for row in morse_list:
        if '-' in row and '.' in row:
            first = min(row.find('.'), row.find('-'))
        elif '-' in row:
            first = row.find('-')
        elif '.' in row:
            first = row.find('.')
        else:  # Must be all letters, so keep str w/o expansion
            new_list.append(row)
            continue
        leading_letters = row[0:first]
        trailing_morse = row[first:]
        for n_dits in range(1, 5):
            morse_char = trailing_morse[0:n_dits]
            morse_tail = trailing_morse[n_dits:]
            try:
                my_char = morse_to_char(morse_char)
            except ValueError:  # letter not found like .-.- so do not add anything
                continue
            new_list.append(leading_letters + my_char + morse_tail)
    return new_list


def full_expand(morse_list):
    """Calculate all possible letter interpretations of a Morse string."""
    for i in range(len(morse_list[0])):
        morse_list = expand_once(morse_list)
        if '-' not in morse_list[0] and '.' not in morse_list[0]:
            # Element 0 always takes the longest & is made of only E and T, so if it's clean, then we're done.
            return set(morse_list)
