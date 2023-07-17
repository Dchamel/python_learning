import unittest
from time import perf_counter

t1 = perf_counter()


def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    dict_ppl = dict(zip(heights, names))
    dict_ppl = dict(sorted(dict_ppl.items(), reverse=True))
    names = [name for name in dict_ppl.values()]
    return names


print(sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170]))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_sortPeople(self):
        expected = ["Mary", "Emma", "John"]
        actual = sortPeople(names=["Mary", "John", "Emma"], heights=[180, 165, 170])
        self.assertEqual(expected, actual)

    def test02_sortPeople(self):
        expected = ["Bob", "Alice", "Bob"]
        actual = sortPeople(names=["Alice", "Bob", "Bob"], heights=[155, 185, 150])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
