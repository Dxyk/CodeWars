def is_valid_ip(string):
    """
    return whether the ipv4 given is valid
    :param string: ip
    :type string: str
    :return: whether the ip is valid
    :rtype: bool

    >>> is_valid_ip('12.255.56.1')
    True
    >>> is_valid_ip('')
    False
    >>> is_valid_ip('abc.def.ghi.jkl')
    False
    >>> is_valid_ip('123.456.789.0')
    False
    >>> is_valid_ip('12.34.56')
    False
    >>> is_valid_ip('12.34.56 .1')
    False
    >>> is_valid_ip('12.34.56.-1')
    False
    >>> is_valid_ip('123.045.067.089')
    False
    """
    return (len(string.split('.')) == 4 and
            all(all([isinstance(x, str) and x.isnumeric() and int(x) >= 0 and
                     x[0] != '0'])
            for x in string.split('.')))
