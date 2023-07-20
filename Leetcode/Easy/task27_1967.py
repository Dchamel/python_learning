import unittest, string
from time import perf_counter

t1 = perf_counter()


def numOfStrings(patterns: list[str], word: str) -> int:
    return len([el for el in patterns if el in word])


print(numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_numOfStrings(self):
        expected = 3
        actual = numOfStrings(patterns=["a", "abc", "bc", "d"], word="abc")
        self.assertEqual(expected, actual)

    def test02_numOfStrings(self):
        expected = 2
        actual = numOfStrings(patterns=["a", "b", "c"], word="aaaaabbbbb")
        self.assertEqual(expected, actual)

    def test03_numOfStrings(self):
        expected = 3
        actual = numOfStrings(patterns=["a", "a", "a"], word="ab")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
