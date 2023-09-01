import unittest
from time import perf_counter

t1 = perf_counter()

"""
2710

Given a positive integer {num} represented as a string, return the integer {num} without trailing zeros as a string.
Constraints:
- {1 <= num.length <= 1000}
- {num} consists of only digits.
- {num} doesn't have any leading zeros.
"""


def removeTrailingZeros(num: str) -> str:
    num_new = ''
    num = num[::-1]
    for i, char in enumerate(num):
        if char == '0':
            continue
        else:
            num_new += num[i:]
            num_new = num_new[::-1]
            break

    return num_new


print(removeTrailingZeros(num="51230100"))


# tests
class AllTests(unittest.TestCase):

    def test00_removeTrailingZeros(self):
        expected = "512301"
        actual = removeTrailingZeros(num="51230100")
        self.assertEqual(expected, actual)

    def test01_removeTrailingZeros(self):
        expected = "123"
        actual = removeTrailingZeros(num="123")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
