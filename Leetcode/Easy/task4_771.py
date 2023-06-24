import unittest
from time import perf_counter

t1 = perf_counter()


def stones_filter(jewels, stones: str) -> int:
    quantity = 0
    for jewel in jewels:
        quantity += stones.count(jewel)

    return quantity


# tests
class AllTestsEasy13(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_oper_proc(self):
        expected = 3
        actual = stones_filter(jewels="aA", stones="aAAbbbb")
        self.assertEqual(expected, actual)

    def test02_oper_proc(self):
        expected = 0
        actual = stones_filter(jewels="z", stones="ZZ")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
