import unittest
from time import perf_counter

t1 = perf_counter()

"""
2108

Given an array of strings {words}, return the first palindromic string in the array. If there is no such string, return an empty string {""}.
A string is palindromic if it reads the same forward and backward.
Constraints:
- {1 <= words.length <= 100}
- {1 <= words[i].length <= 100}
- {words[i]} consists only of lowercase English letters.
"""


def firstPalindrome(words: list[str]) -> str:
    firstPalindrome = ''
    for word in words:
        if len(word) % 2 == 0:
            word_half = word[0:int(len(word) / 2)]
            word_other_half = word[int(len(word) / 2):]
            if word_half == word_other_half[::-1]:
                firstPalindrome = word
                break
        else:
            word_half_odd = word[0:int(len(word) / 2)]
            word_other_half_odd = word[int(len(word) / 2) + 1:]
            if word_half_odd == word_other_half_odd[::-1]:
                firstPalindrome = word
                break
    return firstPalindrome


print(firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"]))


# tests
class AllTests(unittest.TestCase):

    def test00_firstPalindrome(self):
        expected = "ada"
        actual = firstPalindrome(words=["abc", "car", "ada", "racecar", "cool"])
        self.assertEqual(expected, actual)

    def test01_firstPalindrome(self):
        expected = "racecar"
        actual = firstPalindrome(words=["notapalindrome", "racecar"])
        self.assertEqual(expected, actual)

    def test02_firstPalindrome(self):
        expected = ""
        actual = firstPalindrome(words=["def", "ghi"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
