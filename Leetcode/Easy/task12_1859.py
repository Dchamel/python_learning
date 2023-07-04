import unittest
from time import perf_counter

t1 = perf_counter()


def sort_sentence(s: str) -> str:
    q = sorted(s.split(' '), key=lambda x: x[-1])
    sorted_sentence = ' '.join(list(map(lambda x: x[0:-1], q)))
    return sorted_sentence


print(sort_sentence(s="is2 sentence4 This1 a3"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_sort_sentence(self):
        expected = "This is a sentence"
        actual = sort_sentence(s="is2 sentence4 This1 a3")
        self.assertEqual(expected, actual)

    def test02_sort_sentence(self):
        expected = "Me Myself and I"
        actual = sort_sentence(s="Myself2 Me1 I4 and3")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
