import unittest
from time import perf_counter

t1 = perf_counter()

"""
2000

Given a 0-indexed string {word} and a character {ch}, reverse the segment of {word} that starts at index {0} and ends at the index of the first occurrence of {ch} (inclusive). If the character {ch} does not exist in {word}, do nothing.
- For example, if {word = "abcdefd"} and {ch = "d"}, then you should reverse the segment that starts at {0} and ends at {3} (inclusive). The resulting string will be {"dcbaefd"}.
Return the resulting string.
Constraints:
- {1 <= word.length <= 250}
- {word} consists of lowercase English letters.
- {ch} is a lowercase English letter.
"""


def reversePrefix(word: str, ch: str) -> str:
    return (word[word.find(ch)::-1] + word[word.find(ch) + 1:]) if word.find(ch) != -1 else word


# print(reversePrefix(word="abcdefd", ch="d"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test00_reversePrefix(self):
        expected = "dcbaefd"
        actual = reversePrefix(word="abcdefd", ch="d")
        self.assertEqual(expected, actual)

    def test01_reversePrefix(self):
        expected = "zxyxxe"
        actual = reversePrefix(word="xyxzxe", ch="z")
        self.assertEqual(expected, actual)

    def test02_reversePrefix(self):
        expected = "abcd"
        actual = reversePrefix(word="abcd", ch="z")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
