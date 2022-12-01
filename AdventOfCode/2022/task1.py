import unittest
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def list_summ_cal(data):
    elves_data = [0]
    for data_line in data.splitlines():
        if data_line != '':
            elves_data[-1] += int(data_line)
        else:
            elves_data.append(0)
    return elves_data


# tests
class AllTests2022Task1(unittest.TestCase):

    def setUp(self) -> None:
        self.data = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000'

    # tests for part1
    def test01_read_data(self):
        expected = '5'
        actual = read_data('inputs/task1.txt')[12]
        self.assertEqual(expected, actual)

    def test02_cal_for_each(self):
        expected = 6000
        print(list_summ_cal(self.data))
        actual = list_summ_cal(self.data)[0]

        self.assertEqual(expected, actual)

    def test03_cal_for_each(self):
        expected = 4000
        actual = list_summ_cal(self.data)[1]
        self.assertEqual(expected, actual)

    def test04_cal_for_each(self):
        expected = 11000
        actual = list_summ_cal(self.data)[2]
        self.assertEqual(expected, actual)

    def test05_cal_for_each(self):
        expected = 24000
        actual = list_summ_cal(self.data)[3]
        self.assertEqual(expected, actual)

    def test06_cal_for_each(self):
        expected = 10000
        actual = list_summ_cal(self.data)[4]
        self.assertEqual(expected, actual)

    def test07_max_cal(self):
        expected = 24000
        actual = max(list_summ_cal(self.data))
        self.assertEqual(expected, actual)


path = 'inputs/task1.txt'
data = read_data(path)
print(max(list_summ_cal(data)))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
