import unittest
from time import perf_counter
t1 = perf_counter()


class Player(object):
    '''Player'''

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ':\t' + str(self.score)
        return rep


# Test Section
class AllTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Card(self):
        actual = ''
        self.assertEqual(actual, '')


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
