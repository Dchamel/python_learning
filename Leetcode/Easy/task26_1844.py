import unittest, string
from time import perf_counter

t1 = perf_counter()


def replaceDigits(s: str) -> str:
    final_str = ''

    def shift(c: str, x: int) -> str:
        reg_alphabet = list(string.ascii_lowercase)
        letter = reg_alphabet[reg_alphabet.index(c) + x]
        return letter

    for i, l in enumerate(s):
        if s.index(l) % 2 == 0:
            final_str += l
        else:
            final_str += shift(s[i - 1], int(l))

    return final_str


print(replaceDigits(s="a1c1e1"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_replaceDigits(self):
        expected = "abcdef"
        actual = replaceDigits(s="a1c1e1")
        self.assertEqual(expected, actual)

    def test02_replaceDigits(self):
        expected = "abbdcfdhe"
        actual = replaceDigits(s="a1b2c3d4e")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
