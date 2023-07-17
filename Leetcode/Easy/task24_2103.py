import unittest
from time import perf_counter

t1 = perf_counter()


def countPoints(rings: str) -> int:
    rod_list = {}
    for index in range(0, len(rings), 2):
        if rings[index + 1] in rod_list:
            rod_list[rings[index + 1]] += rings[index]
        else:
            rod_list[rings[index + 1]] = rings[index]
    counter = len([each for each in rod_list.values() if ('B' in each and 'G' in each and 'R' in each)])

    return counter


print(countPoints(rings="B0B6G0R6R0R6G9"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_countPoints(self):
        expected = 1
        actual = countPoints(rings="B0B6G0R6R0R6G9")
        self.assertEqual(expected, actual)

    def test02_countPoints(self):
        expected = 1
        actual = countPoints(rings="B0R0G0R9R0B0G0")
        self.assertEqual(expected, actual)

    def test03_countPoints(self):
        expected = 0
        actual = countPoints(rings="G4")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
