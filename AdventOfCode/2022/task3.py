import unittest, string
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def all_let():
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
class AllTests2022Task2(unittest.TestCase):

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


path = 'inputs/task3.txt'
data = read_data(path)
print(part_one(data))
print(part_two(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
