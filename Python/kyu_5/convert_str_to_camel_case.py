def to_camel_case(text):
    """
    return camel cased text. i.e. sLLLLL. LLLLL iff text[i].isupper
    :param text: text
    :type text: str
    :return: camel cased text
    :rtype: str
    """
    if len(text) > 0:
        result = text[0]
        a = 1
        while a < len(text):
            if text[a].isalpha() and text[a - 1].isalpha():
                result += text[a]
            elif text[a].isalpha() and not text[a - 1].isalpha():
                result += text[a].capitalize()
            else:
                result += ''
            a += 1
        return result
    else:
        return ''


def soln_to_camel_case(text):
    return (text[0] + ''.join([w[0].upper() + w[1:]
                               for w in text.replace("_", "-").split("-")])[1:]
            if text else '')
