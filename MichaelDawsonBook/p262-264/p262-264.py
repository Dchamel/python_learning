import unittest
from time import perf_counter
t1 = perf_counter()





# Test Section
class AllTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_Card(self):
        actual = ''
        self.assertEqual(actual, '')


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
