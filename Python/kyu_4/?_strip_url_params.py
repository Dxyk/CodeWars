def strip_url_params(url, params_to_strip = []):
    """

    :param url: url
    :type url: str
    :param params_to_strip: parameters to strip
    :type params_to_strip: list[str]
    :return: stripped url
    :rtype: str

    >>> strip_url_params('www.codewars.com?a=1&b=2&a=2')
    'www.codewars.com?a=1&b=2'
    >>> strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b'])
    'www.codewars.com?a=1'
    >>> strip_url_params('www.codewars.com', ['b'])
    'www.codewars.com'
    """
    # Todo: learn about url
