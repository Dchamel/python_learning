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
class AllTests2022Task6(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path

        self.data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
        self.data2 = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
        self.data3 = 'nppdvjthqldpwncqszvftbrmjlhg'
        self.data4 = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
        self.data5 = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

    def test01_read_data(self):
        expected = 'h'
        actual = read_data(self.path)[3]
        self.assertEqual(expected, actual)

    def test02_part_one(self):
        expected = 7
        actual = part_one(self.data)
        self.assertEqual(expected, actual)

    def test03_part_one(self):
        expected = 5
        actual = part_one(self.data2)
        self.assertEqual(expected, actual)

    def test04_part_one(self):
        expected = 6
        actual = part_one(self.data3)
        self.assertEqual(expected, actual)

    def test05_part_one(self):
        expected = 10
        actual = part_one(self.data4)
        self.assertEqual(expected, actual)

    def test06_part_one(self):
        expected = 11
        actual = part_one(self.data5)
        self.assertEqual(expected, actual)

    def test07_part_two(self):
        expected = 19
        actual = part_two(self.data)
        self.assertEqual(expected, actual)

    def test08_part_two(self):
        expected = 23
        actual = part_two(self.data2)
        self.assertEqual(expected, actual)

    def test09_part_two(self):
        expected = 23
        actual = part_two(self.data3)
        self.assertEqual(expected, actual)

    def test10_part_two(self):
        expected = 29
        actual = part_two(self.data4)
        self.assertEqual(expected, actual)

    def test11_part_two(self):
        expected = 26
        actual = part_two(self.data5)
        self.assertEqual(expected, actual)


path = 'inputs/task6.txt'
data = read_data(path)

print(part_one(data))
print(part_two(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
