import unittest
from time import perf_counter

t1 = perf_counter()


def maxDepth(s: str) -> int:
    q = 0
    list_q = []
    for sym in s:
        if sym == '(':
            q += 1
        elif sym == ')':
            q -= 1
        list_q.append(q)

    return max(list_q)


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
