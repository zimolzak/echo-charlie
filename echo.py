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


