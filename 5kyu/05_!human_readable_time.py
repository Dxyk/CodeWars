def make_readable(seconds):
    """
    return a human readable time in HH:MM:SS form
    :param seconds: time in seconds
    :type seconds: int
    :return: human readable time in HH:MM:SS
    :rtype: str
    """
    ss = seconds % 60
    mm = (seconds // 60) % 60
    hh = (seconds // 60) // 60
    return '{0}:{1}:{2}'.format(hh if hh >= 10 else '0' + str(hh),
                                mm if mm >= 10 else '0' + str(mm),
                                ss if ss >= 10 else '0' + str(ss))


# string formatting
def make_readable_soln(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
