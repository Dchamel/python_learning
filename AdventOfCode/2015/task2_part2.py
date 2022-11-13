import unittest, task2
from time import perf_counter

t1 = perf_counter()


def smallest_perimeter(l, w, h):
    dimensions_sorted = [l, w, h]
    dimensions_sorted.sort()
    smallest_perimeter = 2 * (dimensions_sorted[0] + dimensions_sorted[1])
    return smallest_perimeter


def ribbon_wrap(l, w, h):
    ribbon_wrap = smallest_perimeter(l, w, h)
    return ribbon_wrap


def ribbon_bow(l, w, h):
    ribbon_bow = l * w * h
    return ribbon_bow


def ribbon_total_1parcel(l, w, h):
    ribbon_total = ribbon_wrap(l, w, h) + ribbon_bow(l, w, h)
    return ribbon_total


def ribbon_calculation(data):
    ribbon_summary = 0
    for package in data.splitlines():
        l, w, h = task2.each_package_dimensions(package)
        ribbon_summary += ribbon_total_1parcel(l, w, h)
    return ribbon_summary


path = 'inputs/task2.txt'
data = task2.read_data(path)
print(f'Total Ribbon amount: {ribbon_calculation(data)} feet')


class AllTestsTask2(unittest.TestCase):

    def test1_smallest_perimeter(self):
        actual = smallest_perimeter(1, 2, 3)
        expected = 6
        self.assertEqual(expected, actual)

    def test2_ribbon_wrap(self):
        actual = ribbon_wrap(2, 3, 4)
        expected = 10
        self.assertEqual(expected, actual)

    def test3_ribbon_wrap2(self):
        actual = ribbon_wrap(1, 1, 10)
        expected = 4
        self.assertEqual(expected, actual)

    def test4_ribbon_bow(self):
        actual = ribbon_bow(2, 3, 4)
        expected = 24
        self.assertEqual(expected, actual)

    def test5_ribbon_bow2(self):
        actual = ribbon_bow(1, 1, 10)
        expected = 10
        self.assertEqual(expected, actual)

    def test6_ribbon_total_1parcel(self):
        actual = ribbon_total_1parcel(2, 3, 4)
        expected = 34
        self.assertEqual(expected, actual)

    def test7_ribbon_total_1parcel(self):
        actual = ribbon_total_1parcel(1, 1, 10)
        expected = 14
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
