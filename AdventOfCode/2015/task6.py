import unittest, re
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def coord_from_line(data_line):
    nums = re.findall(r'\d+,\d+', data_line)
    nums_parsed = []
    for each in nums:
        nums_parsed += each.split(',')
    x1, y1, x2, y2 = [int(i) for i in nums_parsed]

    return x1, y1, x2, y2


# matrix [x][y]
def create_matrix(x_num, y_num):
    matrix = [[0] * y_num for _ in range(x_num)]
    for x in range(x_num):
        for y in range(y_num):
            matrix[x][y] = 0
    return matrix


def turn_on(x1, y1, x2, y2, matrix):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] = 1
    return matrix


def turn_off(x1, y1, x2, y2, matrix):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] = 0
    return matrix


def toggle(x1, y1, x2, y2, matrix):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            matrix[x][y] = int(not bool(matrix[x][y]))
    return matrix


def action(data_line, matrix):
    x1, y1, x2, y2 = coord_from_line(data_line)
    if 'turn on' in data_line:
        matrix = turn_on(x1, y1, x2, y2, matrix)
    elif 'turn off' in data_line:
        matrix = turn_off(x1, y1, x2, y2, matrix)
    elif 'toggle' in data_line:
        matrix = toggle(x1, y1, x2, y2, matrix)

    return matrix


def main_prog(data):
    matrix = create_matrix(1000, 1000)

    for data_line in data.splitlines():
        matrix = action(data_line, matrix)

    total_lights = 0
    for row in matrix:
        for value in row:
            if value == 1:
                total_lights += 1
    return total_lights


# tests
class AllTestsTask5(unittest.TestCase):

    # tests for part1
    def test01_read_data(self):
        expected = '6'
        actual = read_data('inputs/task6.txt')[8]
        self.assertEqual(expected, actual)

    def test02_coord_from_line(self):
        expected = 808
        actual = coord_from_line('turn off 735,808 through 917,910')[1]
        self.assertEqual(expected, actual)

    def test03_main_prog(self):
        expected = 1000000
        actual = main_prog('turn on 0,0 through 999,999')
        self.assertEqual(expected, actual)

    def test04_main_prog(self):
        expected = 1000
        actual = main_prog('toggle 0,0 through 999,0')
        self.assertEqual(expected, actual)


path = 'inputs/task6.txt'
data = read_data(path)
print(main_prog(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
