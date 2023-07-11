import unittest
from time import perf_counter

t1 = perf_counter()


def maxDepth(s: str) -> int:
    q = 0

    def counter(i: str) -> int:
        nonlocal q
        if i == '(':
            q += 1
        elif i == ')':
            q -= 1
        return q

    q_list = max([counter(i) for i in s])
    return q_list


# (1(2(3)2)1(2(3(4(5)4)3(4)3)2)1)

print(maxDepth(s="(1+(2*3)+((8)/4))+1"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_maxDepth(self):
        expected = 3
        actual = maxDepth(s="(1+(2*3)+((8)/4))+1")
        self.assertEqual(expected, actual)

    def test02_maxDepth(self):
        expected = 3
        actual = maxDepth(s="(1)+((2))+(((3)))")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
