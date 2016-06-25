class RomanNumerals:
    # TODO: What to do with init?
    # TODO: unbound method to_roman() must be called with RomanNumerals instance
    # TODO: as first argument (got int instance instead)
    """Convert roman num to and from numeral num."""

    def to_roman(self, n):
        """
        Turn the numeral number into roman number.
        I: 1; V: 5; X: 10; L: 50; C: 100; D: 500; M: 1000
        :param n: numeral number
        :type n: int
        :return: roman number
        :rtype: str

        >>> RomanNumerals().to_roman(1)
        'I'
        >>> RomanNumerals().to_roman(4)
        'IV'
        >>> RomanNumerals().to_roman(6)
        'VI'
        >>> RomanNumerals().to_roman(21)
        'XXI'
        """
        roman_numerals = {1000: 'M',
                          900: 'CM',
                          500: 'D',
                          400: 'CD',
                          100: 'C',
                          90: 'XC',
                          50: 'L',
                          40: 'XL',
                          10: 'X',
                          9: 'IX',
                          5: 'V',
                          4: 'IV',
                          1: 'I'
                          }
        roman_string = ''
        for key in sorted(roman_numerals.keys(), reverse = True):
            while n >= key:
                roman_string += roman_numerals[key]
                n -= key
        return roman_string

    def from_roman(self, roman):
        """
        Turn the roman numeral into an integer.
        I: 1; V: 5; X: 10; L: 50; C: 100; D: 500; M: 1000
        :param roman: roman numeral
        :type roman: str
        :return: integer
        :rtype: int

        >>> RomanNumerals().from_roman('MCMXLIII')
        1943
        """
        roman_int = \
            {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if len(roman) == 0:
            return 0
        elif len(roman) == 1:
            return roman_int[roman]
        else:
            result = 0
            i = 1
            temp = 0
            minus = 0
            while i < len(roman):
                if roman_int[roman[i]] <= roman_int[roman[i - 1]]:
                    temp += roman_int[roman[i - 1]]
                    result += temp
                    temp = 0
                else:
                    temp += roman_int[roman[i - 1]]
                    result -= temp
                    temp = 0
                i += 1
            return result + temp - minus + roman_int[roman[-1]]
