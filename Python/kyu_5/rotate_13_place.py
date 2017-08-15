def rot13(message):
    """
    rotate each letter in the message by 13 place

    :param message: message
    :type message: str
    :return: rotated message
    :rtype: str

    >>> rot13("EBG13 rknzcyr.")
    'ROT13 example.'
    >>> rot13('a z m A Z M')
    'n m z N M Z'
    """
    result = ''
    for s in message:
        if s.isalpha() and s.islower():
            result += chr(ord(s) + 13) if ord(s) <= 109 else chr(ord(s) - 13)
        elif s.isalpha() and s.isupper():
            result += chr(ord(s) + 13) if ord(s) <= 77 else chr(ord(s) - 13)
        else:
            result += s
    return result


def rot13_soln(message):
    return message.encode('rot13')
