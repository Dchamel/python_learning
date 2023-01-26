import unittest
from time import perf_counter

t1 = perf_counter()


def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')


# tests
class AllTestsEasy1108(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_defangIPaddr(self):
        expected = "1[.]1[.]1[.]1"
        actual = defangIPaddr("1.1.1.1")
        self.assertEqual(expected, actual)


print(defangIPaddr("255.100.50.0"))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
