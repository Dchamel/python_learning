import unittest
from time import perf_counter

t1 = perf_counter()

"""
344

Write a function that reverses a string. The input string
is given as an array of characters {s}.
You must do this by modifying the input arrayin-placewith
 {O(1)} extra memory.
Constraints:
- {1 <= s.length <= 10^5}
- {s[i]} is aprintable ascii character.
"""


def reverseString(s: list[str]) -> None:
    """
    This func modify `s` in-place.
    `return` only for testcases below
    """
    s1 = '%'.join(s)[::-1].split('%')
    for i in range(len(s)):
        s[i] = s1[i]

    return s


print(reverseString(s=["h", "e", "l", "l", "o"]))


# tests
class AllTests(unittest.TestCase):

    def test00_reverseString(self):
        expected = ["o", "l", "l", "e", "h"]
        actual = reverseString(s=["h", "e", "l", "l", "o"])
        self.assertEqual(expected, actual)

    def test01_reverseString(self):
        expected = ["h", "a", "n", "n", "a", "H"]
        actual = reverseString(s=["H", "a", "n", "n", "a", "h"])
        self.assertEqual(expected, actual)

    def test02_reverseString(self):
        expected = ["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ", "a", " ", ",", "n", "a", "l",
                    "p", " ", "a", " ", ",", "n", "a", "m", " ", "A"]
        actual = reverseString(
            s=["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a",
               "l", ":",
               " ", "P", "a", "n", "a", "m", "a"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
