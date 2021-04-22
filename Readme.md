# Echo Charlie

Echo Charlie is a simple Python function to replace string letters
with their NATO/ICAO phonetic alphabet equivalents. The silliness
comes when you apply it twice in a row.

    >>> from echo import echo
    >>> echo('Hello')
    'Hotel echo lima lima oscar '
    >>> echo(echo('Hello'))
    'Hotel oscar tango echo lima, echo charlie hotel oscar, lima india
    mike alfa, lima india mike alfa, oscar sierra charlie alfa romeo,    '
