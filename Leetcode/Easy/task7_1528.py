import unittest
from time import perf_counter

t1 = perf_counter()


def order_string(s, indices):
    s = list(s)
    working_dict = dict(zip(indices, s))
    working_dict = dict(sorted(working_dict.items()))
    result = ''.join(working_dict.values())
    return result


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_order_string(self):
        expected = "leetcode"
        actual = order_string(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3])
        self.assertEqual(expected, actual)

    def test02_order_string(self):
        expected = "abc"
        actual = order_string(s="abc", indices=[0, 1, 2])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
