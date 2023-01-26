import unittest
from time import perf_counter

t1 = perf_counter()


def romanToInt(s: str) -> int:
    romint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_s = 0
    for index, each in enumerate(s):
        try:
            if each == 'I' and s[index + 1] == 'V':
                int_s += 4
                s = s[index + 2:]
                print('1')
            elif each == 'I' and s[index + 1] == 'X':
                int_s += 9
                s = s[index + 2:]
            elif each == 'X' and s[index + 1] == 'L':
                int_s += 40
                s = s[index + 2:]
            elif each == 'X' and s[index + 1] == 'C':
                int_s += 80
                s = s[index + 2:]
            elif each == 'C' and s[index + 1] == 'D':
                int_s += 400
                s = s[index + 2:]
            elif each == 'C' and s[index + 1] == 'M':
                int_s += 900
                s = s[index + 2:]
            else:
                int_s += romint[each]

        except:
            pass

    return int_s


print(romanToInt("IV"))


# tests
class AllTestsEasy13(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_romanToInt(self):
        expected = 4
        actual = romanToInt("IV")
        self.assertEqual(expected, actual)

    def test02_romanToInt(self):
        expected = 9
        actual = romanToInt("IX")
        self.assertEqual(expected, actual)

    # def test03_romanToInt(self):
    #     expected = 1994
    #     actual = romanToInt("MCMXCIV")
    #     self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
