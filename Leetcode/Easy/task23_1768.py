import unittest
from time import perf_counter

t1 = perf_counter()


def mergeAlternately(word1: str, word2: str) -> str:
    new_str = ''
    for i, l in enumerate(word1):
        try:
            new_str += l + word2[i]
        except:
            break
    if len(word1) < len(word2):
        new_str += word2[i + 1:]
    elif len(word1) > len(word2):
        new_str += word1[i:]
    return new_str


print(mergeAlternately(word1="abcd", word2="pq"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_mergeAlternately(self):
        expected = "apbqcr"
        actual = mergeAlternately(word1="abc", word2="pqr")
        self.assertEqual(expected, actual)

    def test02_mergeAlternately(self):
        expected = "apbqrs"
        actual = mergeAlternately(word1="ab", word2="pqrs")
        self.assertEqual(expected, actual)

    def test03_mergeAlternately(self):
        expected = "apbqcd"
        actual = mergeAlternately(word1="abcd", word2="pq")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
