import unittest
from time import perf_counter

t1 = perf_counter()


def trunc_sent(s: str, k: int) -> str:
    return ' '.join(s.split(' ')[0:k])


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_trunc_sent(self):
        expected = "Hello how are you"
        actual = trunc_sent(s="Hello how are you Contestant", k=4)
        self.assertEqual(expected, actual)

    def test02_trunc_sent(self):
        expected = "What is the solution"
        actual = trunc_sent(s="What is the solution to this problem", k=4)
        self.assertEqual(expected, actual)

    def test03_trunc_sent(self):
        expected = "chopper is not a tanuki"
        actual = trunc_sent(s="chopper is not a tanuki", k=5)
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
