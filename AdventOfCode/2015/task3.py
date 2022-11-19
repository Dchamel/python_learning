import unittest
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        data = rawData.read()
    return data


def santa_step(direction, x, y):
    if direction == '>':
        x += 1
    elif direction == '<':
        x -= 1
    elif direction == '^':
        y += 1
    elif direction == 'v':
        y -= 1
    return x, y


def delivery_path(data: str) -> set:
    x = 0
    y = 0
    coord = [(x, y)]
    delivery_path = set(coord)
    for direction in data:
        x, y = santa_step(direction, x, y)
        coord = (x, y)
        delivery_path.add(coord)
    return delivery_path


def two_ways(data):
    data_santa = ''
    data_robo_santa = ''
    for index, direction in enumerate(data, start=0):
        if index % 2 != 0:  # odd
            data_santa += direction
        else:  # even
            data_robo_santa += direction
    return data_santa, data_robo_santa


# tests
class AllTestsTask3(unittest.TestCase):

    # tests for part1
    def test1_read_data(self):
        expected = 'v'
        actual = read_data('inputs/task3.txt')[3]
        self.assertEqual(expected, actual)

    def test2_santa_step(self):
        expected = (1, 0)
        actual = santa_step('>', 0, 0)
        self.assertEqual(expected, actual)

    def test3_delivered_presents1(self):
        expected = 2
        actual = len(delivery_path('>'))
        self.assertEqual(expected, actual)

    def test3_delivered_presents2(self):
        expected = 4
        actual = len(delivery_path('^>v<'))
        self.assertEqual(expected, actual)

    def test3_delivered_presents3(self):
        expected = 2
        actual = len(delivery_path('^v^v^v^v^v'))
        self.assertEqual(expected, actual)

    # tests for part2
    def test4_delivered_presents_santa_and_robo1(self):
        expected = 3
        data_santa, data_robo_santa = two_ways('^v')
        actual = len(delivery_path(data_santa).union(delivery_path(data_robo_santa)))
        self.assertEqual(expected, actual)

    def test4_delivered_presents_santa_and_robo2(self):
        expected = 3
        data_santa, data_robo_santa = two_ways('^>v<')
        actual = len(delivery_path(data_santa).union(delivery_path(data_robo_santa)))
        self.assertEqual(expected, actual)

    def test4_delivered_presents_santa_and_robo3(self):
        expected = 11
        data_santa, data_robo_santa = two_ways('^v^v^v^v^v')
        actual = len(delivery_path(data_santa).union(delivery_path(data_robo_santa)))
        self.assertEqual(expected, actual)


path = 'inputs/task3.txt'
data = read_data(path)

# part1
print(f'Delivered presents by Santa: {len(delivery_path(data))}')

# part2
data_santa, data_robo_santa = two_ways(data)
delivery_path_santa = delivery_path(data_santa)
delivery_path_robo_santa = delivery_path(data_robo_santa)
new_path = delivery_path_santa.union(delivery_path_robo_santa)
print(f'Delivered presents by Santa and his Robo: {len(new_path)}')

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
