def pig_it(text):
    """
    turn text to latin by reversing and adding 'ay' at the end of word
    :param text: english text
    :type text: str
    :return: latin text
    :rtype: str

    >>> pig_it('Pig latin is cool')
    'igPay atinlay siay oolcay'
    """
    return ' '.join([s[1:] + s[0] + 'ay' if s.isalpha() else s
                     for s in text.split()])
