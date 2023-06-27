import unittest
from time import perf_counter

t1 = perf_counter()


def counter(items: list, ruleKey: str, ruleValue: str) -> int:
    count_val = 0

    return count_val


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_counter(self):
        expected = 1
        actual = counter(
            items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
            ruleKey="color", ruleValue="silver")
        self.assertEqual(expected, actual)

    def test02_counter(self):
        expected = 2
        actual = counter(
            items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
            ruleKey="type", ruleValue="phone")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
