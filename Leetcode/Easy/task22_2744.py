import unittest
from time import perf_counter

t1 = perf_counter()


def maximumNumberOfStringPairs(words: list[str]) -> int:
    max_num = 0
    for index, each in enumerate(words):
        if each[::-1] in words[index + 1:]:
            if index != len(words) - 1:
                max_num += 1
    return max_num


print(maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"]))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_maximumNumberOfStringPairs(self):
        expected = 2
        actual = maximumNumberOfStringPairs(words=["cd", "ac", "dc", "ca", "zz"])
        self.assertEqual(expected, actual)

    def test02_maximumNumberOfStringPairs(self):
        expected = 1
        actual = maximumNumberOfStringPairs(words=["ab", "ba", "cc"])
        self.assertEqual(expected, actual)

    def test03_maximumNumberOfStringPairs(self):
        expected = 0
        actual = maximumNumberOfStringPairs(words=["aa", "ab"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
