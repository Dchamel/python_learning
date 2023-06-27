import unittest
from time import perf_counter

import re

t1 = perf_counter()


def counter(items: list, ruleKey: str, ruleValue: str) -> int:
    keys = ['type', 'color', 'name']
    i = keys.index(ruleKey)
    counter_val = len([item for item in items if re.search(rf'^{ruleValue}$', item[i])])
    
    return counter_val


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

    def test03_counter(self):
        expected = 0
        actual = counter(
            items=[["ii", "iiiiiii", "ii"], ["iiiiiii", "iiiiiii", "ii"], ["ii", "iiiiiii", "iiiiiii"]],
            ruleKey="color", ruleValue="ii")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
