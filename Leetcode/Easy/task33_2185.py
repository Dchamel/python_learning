import unittest
from time import perf_counter

t1 = perf_counter()

"""
2185

You are given an array of strings {words} and a string {pref}.
Return the number of strings in {words} that contain {pref} as a prefix.
A prefix of a string {s} is any leading contiguous substring of {s}.
Constraints:
- {1 <= words.length <= 100}
- {1 <= words[i].length, pref.length <= 100}
- {words[i]} and {pref} consist of lowercase English letters.
"""


def prefixCount(words: list[str], pref: str) -> int:
    """Return the number of strings in words that contain pref as a prefix."""
    i = 0
    for word in words:
        if word.startswith(pref):
            i += 1
        else:
            continue
    return i


print(prefixCount(words=["pay", "attention", "practice", "attend"], pref="at"))


# tests
class AllTests(unittest.TestCase):

    def test00_prefixCount(self):
        expected = 2
        actual = prefixCount(words=["pay", "attention", "practice", "attend"], pref="at")
        self.assertEqual(expected, actual)

    def test01_prefixCount(self):
        expected = 0
        actual = prefixCount(words=["leetcode", "win", "loops", "success"], pref="code")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
