import unittest
from time import perf_counter

t1 = perf_counter()


def equiv_arr(word1: list, word2: list) -> bool:
    return ''.join(word1) == ''.join(word2)


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_equiv_arr(self):
        expected = True
        actual = equiv_arr(word1=["ab", "c"], word2=["a", "bc"])
        self.assertEqual(expected, actual)

    def test02_equiv_arr(self):
        expected = False
        actual = equiv_arr(word1=["a", "cb"], word2=["ab", "c"])
        self.assertEqual(expected, actual)

    def test03_equiv_arr(self):
        expected = True
        actual = equiv_arr(word1=["abc", "d", "defg"], word2=["abcddefg"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
