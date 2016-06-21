import unittest
from kyu_4.roman_numeral_decoder import solution


class TestRomanNumeralDecoder(unittest.TestCase):
    """ Test the Roman Numeral Decoder """

    def test_one_numeral(self):
        self.assertEqual(solution('C'), 100, 'C should be 100')

    def test_same_level_concatenation(self):
        self.assertEqual(solution('II'), 2, 'II should be 2')

    def test_same_level_concatenation_2(self):
        self.assertEqual(solution('MM'), 2000, 'CC should be 200')

    def test_two_consecutive_level_concatenation_plus(self):
        self.assertEqual(solution('VI'), 6, 'VI should be 5 + 1 = 6')

    def test_two_consecutive_level_concatenation_plus_2(self):
        self.assertEqual(solution('DC'), 600, 'DC should be 500 + 100 = 600')

    def test_two_consecutive_level_concatenation_minus(self):
        self.assertEqual(solution('IV'), 4, 'IV should be 5 - 1 = 6')

    def test_two_consecutive_level_concatenation_minus_2(self):
        self.assertEqual(solution('CD'), 400, 'CD should be 500 - 100 = 400')

    def test_three_level_concatenation(self):
        self.assertEqual(solution('MIV'), 1004, 'MIV should be 1000 + 5 - 1 = 1004')

    def test_more_level_concatenation(self):
        self.assertEqual(solution('MCMXLIII'), 1943,
                         'MCMXLIII should be 1000 + 900 + 43 = 1943')

if __name__ == "__main__":
    unittest.main()
