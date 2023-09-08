import unittest
from time import perf_counter

t1 = perf_counter()

"""
1704

You are given a string {s} of even length. Split this string into two halves of equal lengths, and let {a} be the first half and {b} be the second half.
Two strings are alike if they have the same number of vowels ({'a'}, {'e'}, {'i'}, {'o'}, {'u'}, {'A'}, {'E'}, {'I'}, {'O'}, {'U'}). Notice that {s} contains uppercase and lowercase letters.
Return {true} if {a} and {b} are alike. Otherwise, return {false}.
Constraints:
- {2 <= s.length <= 1000}
- {s.length} is even.
- {s} consists of uppercase and lowercase letters.
"""


def halvesAreAlike(s: str) -> bool:
    """s: even str
    This func divide 's' on two strings
    Return true if they have the same number of vowels.
    Otherwise, return false.
    """
    vovels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    a = s[:int(len(s) / 2)]
    b = s[int(len(s) / 2):]
    i = 0
    for letter in a:
        if letter in vovels:
            i += 1
        else:
            continue
    j = 0
    for letter in b:
        if letter in vovels:
            j += 1
        else:
            continue
    return True if i == j else False


print(halvesAreAlike(s="book"))


# tests
class AllTests(unittest.TestCase):

    def test00_halvesAreAlike(self):
        expected = True
        actual = halvesAreAlike(s="book")
        self.assertEqual(expected, actual)

    def test01_halvesAreAlike(self):
        expected = False
        actual = halvesAreAlike(s="textbook")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
