import unittest
from time import perf_counter

t1 = perf_counter()


def oper_proc(operations):
    number = 0
    for each in operations:
        if each == '++X' or each == 'X++':
            number += 1
        else:
            number -= 1
    return number


# tests
class AllTestsEasy13(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_oper_proc(self):
        expected = 1
        actual = oper_proc(["--X", "X++", "X++"])
        self.assertEqual(expected, actual)

    def test02_oper_proc(self):
        expected = 3
        actual = oper_proc(["++X", "++X", "X++"])
        self.assertEqual(expected, actual)

    def test03_oper_proc(self):
        expected = 0
        actual = oper_proc(["X++", "++X", "--X", "X--"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
