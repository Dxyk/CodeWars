import re
# WTF is re??

def domain_name(url):
    """
    parse the domain name from a given url
    :param url: the url given
    :type url: str
    :return: the domain name
    :rtype: str

    >>> domain_name("http://github.com/carbonfive/raygun")
    'github'
    >>> domain_name("http://www.zombie-bites.com")
    'zombie-bites'
    >>> domain_name("https://www.cnet.com")
    'cnet'
    >>> domain_name('ww.xakep.r')
    'xakep'
    """
    if 'ww.' not in url[: url.find('.') + 1]:
        if '//' in url:
            return url[url.find('//') + 2: url.find('.')]
        else:
            return url[: url.find('.')]
    else:
        return url[url.find('.') + 1: url.find('.', url.find('.') + 1)]


def soln_domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group(
        'name')
