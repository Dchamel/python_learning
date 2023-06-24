import unittest
from time import perf_counter

t1 = perf_counter()


def max_words_counter(sentences: list):
    quantity_list = []
    for sentence in sentences:  # type: str
        quantity_list.append(len(sentence.split(' ')))
    return max(quantity_list)


# tests
class AllTestsEasy13(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_oper_proc(self):
        expected = 6
        actual = max_words_counter(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
        self.assertEqual(expected, actual)

    def test02_oper_proc(self):
        expected = 3
        actual = max_words_counter(["please wait", "continue to fight", "continue to win"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
