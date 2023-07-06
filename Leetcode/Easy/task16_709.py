import unittest
from time import perf_counter

t1 = perf_counter()


def to_lower_case(s: str) -> str:
    return s.lower()


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_to_lower_case(self):
        expected = "hello"
        actual = to_lower_case(s="Hello")
        self.assertEqual(expected, actual)

    def test02_to_lower_case(self):
        expected = "here"
        actual = to_lower_case(s="here")
        self.assertEqual(expected, actual)

    def test03_to_lower_case(self):
        expected = "lovely"
        actual = to_lower_case(s="LOVELY")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
