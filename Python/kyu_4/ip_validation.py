def is_valid_ip(string):
    return (len(string.split('.')) == 4 and
            all(all(
                [isinstance(x, str) and x.isnumeric() and 255 >= int(x) >= 0 and
                 x[0] != '0'])
                for x in string.split('.')))
