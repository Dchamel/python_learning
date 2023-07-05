import unittest, string
from time import perf_counter

t1 = perf_counter()


def pangram_checker(sentence: str) -> bool:
    if sorted(set(sentence)) == list(string.ascii_lowercase):
        return True
    else:
        return False


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_pangram_checker(self):
        expected = True
        actual = pangram_checker(sentence="thequickbrownfoxjumpsoverthelazydog")
        self.assertEqual(expected, actual)

    def test02_pangram_checker(self):
        expected = False
        actual = pangram_checker(sentence="leetcode")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
