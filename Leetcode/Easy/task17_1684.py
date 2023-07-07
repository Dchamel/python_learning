import unittest
from time import perf_counter

t1 = perf_counter()


def counter_cons_str(allowed: str, words: list) -> int:
    total = 0
    w = 0
    for word in words:
        for letter in word:
            if letter not in allowed:
                w = 1
                break
        if w == 1:
            w = 0
            continue
        else:
            total += 1
            continue

    return total


print(counter_cons_str(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"]))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_counter_cons_str(self):
        expected = 2
        actual = counter_cons_str(allowed="ab", words=["ad", "bd", "aaab", "baa", "badab"])
        self.assertEqual(expected, actual)

    def test02_counter_cons_str(self):
        expected = 7
        actual = counter_cons_str(allowed="abc", words=["a", "b", "c", "ab", "ac", "bc", "abc"])
        self.assertEqual(expected, actual)

    def test03_counter_cons_str(self):
        expected = 4
        actual = counter_cons_str(allowed="cad", words=["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
