import unittest, string
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def all_let():
    '''Alphabet in lower/upper case'''
    low_let = []
    for i in string.ascii_lowercase:
        low_let.append(i)
    up_let = []
    for i in string.ascii_uppercase:
        up_let.append(i)
    all_let = low_let + up_let

    return all_let


def wrong_item(data_line):
    half_string_index = int(len(data_line) / 2)
    first_compartment = data_line[0:half_string_index]
    second_compartment = data_line[half_string_index:]
    wrong_item = list(set(first_compartment).intersection(set(second_compartment)))[0]

    return wrong_item


def part_one(data):
    all_items = all_let()
    property_summ = 0
    for data_line in data.splitlines():
        item = wrong_item(data_line)
        priority = all_items.index(item) + 1
        property_summ += priority

    return property_summ


def common_value_list(data):
    common_value_list = []
    data_lines = data.splitlines()
    while data_lines:
        elf1, elf2, elf3 = data_lines[0:3]
        del data_lines[0:3]
        common_value = set(elf1) & set(elf2) & set(elf3)
        common_value_list += common_value

    return common_value_list


def part_two(data):
    priority_summ = 0
    for each in common_value_list(data):
        priority_summ += all_let().index(each) + 1
    return priority_summ


# tests
class AllTests2022Task3(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path
        self.data = 'vJrwpWtwJgWrhcsFMMfFFhFp\n' \
                    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n' \
                    'PmmdzqPrVvPwwTWBwg\n' \
                    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n' \
                    'ttgJtRGJQctTZtZT\n' \
                    'CrZsJsPPZsGzwwsLwLmpwMDw'

    def test01_read_data(self):
        expected = 's'
        actual = read_data(self.path)[3]
        self.assertEqual(expected, actual)

    def test02_wrong_item(self):
        expect = 'p'
        reality = wrong_item(self.data.splitlines()[0])
        self.assertEqual(expect, reality)

    def test03_wrong_item(self):
        expect = 'L'
        reality = wrong_item(self.data.splitlines()[1])
        self.assertEqual(expect, reality)

    def test04_wrong_item(self):
        expect = 'P'
        reality = wrong_item(self.data.splitlines()[2])
        self.assertEqual(expect, reality)

    def test05_wrong_item(self):
        expect = 'v'
        reality = wrong_item(self.data.splitlines()[3])
        self.assertEqual(expect, reality)

    def test06_wrong_item(self):
        expect = 't'
        reality = wrong_item(self.data.splitlines()[4])
        self.assertEqual(expect, reality)

    def test07_wrong_item(self):
        expect = 's'
        reality = wrong_item(self.data.splitlines()[5])
        self.assertEqual(expect, reality)

    def test08_part_one(self):
        expect = 157
        reality = part_one(self.data)
        self.assertEqual(expect, reality)

    def test09_common_value_list(self):
        expect = ['r', 'Z']
        reality = common_value_list(self.data)
        self.assertEqual(expect, reality)

    def test10_part_two(self):
        expect = 70
        reality = part_two(self.data)
        self.assertEqual(expect, reality)


path = 'inputs/task3.txt'
data = read_data(path)
print(part_one(data))
print(part_two(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
