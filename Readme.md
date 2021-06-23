# Echo Charlie

Echo Charlie is a collection of Python functions to mess about with Morse
code and phonetic alphabets.

One function will replace string letters
with their NATO/ICAO phonetic alphabet equivalents. The silliness
comes when you apply it twice in a row.

    >>> from echo import echo
    >>> echo('Hello')
    'Hotel echo lima lima oscar '
    >>> echo(echo('Hello'))
    'Hotel oscar tango echo lima, echo charlie hotel oscar, lima india
    mike alfa, lima india mike alfa, oscar sierra charlie alfa romeo,    '

Another function will take an unspaced Morse string and find out all the
letter strings that it could possibly represent.

    >>> from echo import full_expand
    >>> full_expand(['--..'])
    {'ge', 'mee', 'mi', 'td', 'tne', 'ttee', 'tti', 'z'}
