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

    print(delivery_path)
    return delivery_path

def delivered_presents(delivery_path):
    return len(delivery_path)


def two_ways(data):
    data_santa = ''
    data_robo_santa = ''
    for index, direction in enumerate(data, start=0):
        if index == 0:
            data_santa += direction
            data_robo_santa += direction
            print(f'Santa (Index0/Data): {index, data_santa}')
            print(f'Robo Santa (Index0/Data): {index, data_robo_santa}')
        elif index % 2 != 0: #odd
            data_santa += direction
            print(f'Santa (Index/Data): {index, data_santa}')
        else: #even
            data_robo_santa += direction
            print(f'Robo Santa (Index/Data): {index, data_robo_santa}')
    return data_santa, data_robo_santa


# tests
class AllTestsTask3(unittest.TestCase):

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
        actual = delivered_presents('>')
        self.assertEqual(expected, actual)

    def test3_delivered_presents2(self):
        expected = 4
        actual = delivered_presents('^>v<')
        self.assertEqual(expected, actual)

    def test3_delivered_presents3(self):
        expected = 2
        actual = delivered_presents('^v^v^v^v^v')
        self.assertEqual(expected, actual)


path = 'inputs/task3.txt'
# data = read_data(path)
data = '^v'
data_santa, data_robo_santa = two_ways(data)
print(data_santa)
print(data_robo_santa)

delivery_path_santa = delivery_path(data_santa)
delivery_path_robo_santa = delivery_path(data_robo_santa)

new_path = delivery_path_santa.union(delivery_path_robo_santa)
print(new_path)
print(len(new_path))



# delivery_path = delivery_path(data)
# q = delivered_presents(data_santa)
# w = delivered_presents(data_robo_santa)
# c = delivered_presents('^v')
# print(f'Test: {c}')
# print(f'Santa:{q} Robo Santa: {w}')
# print(f'Delivered presents: {q+w}')

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
