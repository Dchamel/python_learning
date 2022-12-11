import unittest
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def part_one(data):
    for i in range(len(data)):
        if len(set(data[i:i + 4])) == 4:
            return i + 4


def part_two(data):
    for i in range(len(data)):
        if len(set(data[i:i + 14])) == 14:
            return i + 14


# tests - not implemented
class AllTests2022Task2(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path
        self.data = ''

    def test01_read_data(self):
        expected = 's'
        actual = read_data(self.path)[3]
        self.assertEqual(expected, actual)


path = 'inputs/task6.txt'
data = read_data(path)

print(part_one(data))
print(part_two(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
