import unittest
from time import perf_counter

t1 = perf_counter()


def romanToInt(s: str) -> int:
    romint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_s = 0
    vrem = ''

    for i in range(len(s)):
        try:
            next_val = romint[s[i + 1]]
        except:
            next_val = 0
        if romint[s[i]] >= next_val:
            if vrem:
                int_s += romint[s[i]] - romint[vrem]
                vrem = ''
            else:
                int_s += romint[s[i]]
        else:
            vrem = s[i]
            continue

    return int_s


print(romanToInt("LVIII"))


# tests
class AllTestsEasy13(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_romanToInt(self):
        expected = 3
        actual = romanToInt("III")
        self.assertEqual(expected, actual)

    def test02_romanToInt(self):
        expected = 58
        actual = romanToInt("LVIII")
        self.assertEqual(expected, actual)

    def test03_romanToInt(self):
        expected = 1994
        actual = romanToInt("MCMXCIV")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
