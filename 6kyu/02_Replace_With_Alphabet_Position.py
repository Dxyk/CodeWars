def alphabet_position(text):
    """
    Replace each letter into the alphabetical index number.
    Ignore non-strings

    :param text: Text waiting to be transformed
    :type text: str
    :return: returned text
    :rtype: str
    """
    s = [e.lower() for e in text if e.isalpha()]
    return ' '.join([str(ord(x) - 96) for x in s]).rstrip()



if __name__ == '__main__':
    print('')
