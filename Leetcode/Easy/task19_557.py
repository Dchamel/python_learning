import unittest
from time import perf_counter

t1 = perf_counter()


def reverseWords(s: str) -> str:
    return ' '.join([word[::-1] for word in s.split(' ')])


print(reverseWords(s="Let's take LeetCode contest"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_reverseWords(self):
        expected = "s'teL ekat edoCteeL tsetnoc"
        actual = reverseWords(s="Let's take LeetCode contest")
        self.assertEqual(expected, actual)

    def test02_reverseWords(self):
        expected = "doG gniD"
        actual = reverseWords(s="God Ding")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
