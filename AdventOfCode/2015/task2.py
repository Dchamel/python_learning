import unittest
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        data = rawData.read()
    return data


def each_package_dimensions(package):
    # get line and data from it, surface calculation
    l, w, h = [int(i) for i in package.split('x')]
    return l, w, h


def smallest_area(l, w, h):
    first = l * w
    second = w * h
    third = h * l
    smallest = min(first, second, third)
    return smallest


def paper_amount(data):
    # calculate summary quantity of a paper
    paper_amount = 0
    for package in data.splitlines():
        l, w, h = each_package_dimensions(package)
        surface = 2 * l * w + 2 * w * h + 2 * h * l
        paper_amount += surface + smallest_area(l, w, h)

    return paper_amount


path = 'inputs/task2.txt'
data = read_data(path)
print(paper_amount(data))


# tests
class AllTestsTask2(unittest.TestCase):

    def test1_read_data(self):
        actual = read_data('inputs/task2.txt').splitlines()[1]
        expected = '15x27x5'
        self.assertEqual(actual, expected)

    def test2_each_package_surface(self):
        actual = each_package_dimensions('2x3x4')[1]
        expected = 3
        self.assertEqual(actual, expected)

    def test3_smallest_area(self):
        actual = smallest_area(1, 26, 4)
        expected = 4
        self.assertEqual(actual, expected)

    def test4_paper_amount(self):
        actual = paper_amount('2x3x4')
        expected = 58
        self.assertEqual(actual, expected)

        actual = paper_amount('1x1x10')
        expected = 43
        self.assertEqual(actual, expected)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
