import unittest
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def elf_section_list_each(elf):
    elf_section_list = []
    for i in range(int(elf[0]), int(elf[1]) + 1):
        elf_section_list.append(i)
    return elf_section_list


def elf_section_list_all(data_line):
    data_line = data_line.split(',')
    elf1 = data_line[0].split('-')
    elf2 = data_line[1].split('-')
    elf1 = elf_section_list_each(elf1)
    elf2 = elf_section_list_each(elf2)
    return elf1, elf2


def part_one(data):
    count = 0
    for data_line in data.splitlines():
        elf1, elf2 = elf_section_list_all(data_line)
        if not (set(elf1).difference(set(elf2)) and set(elf2).difference(set(elf1))):
            count += 1
    return count


def part_two(data):
    counter = 0
    for data_line in data.splitlines():
        elf1, elf2 = elf_section_list_all(data_line)
        if set(elf1).intersection(set(elf2)):
            counter += 1
    return counter


# tests
class AllTests2022Task4(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path
        self.data = '2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8'

    def test01_read_data(self):
        expected = '9'
        actual = read_data(self.path)[3]
        self.assertEqual(expected, actual)

    def test02_part_one(self):
        expected = 2
        actual = part_one(self.data)
        self.assertEqual(expected, actual)

    def test03_part_two(self):
        expected = 4
        actual = part_two(self.data)
        self.assertEqual(expected, actual)


path = 'inputs/task4.txt'
data = read_data(path)
print(part_one(data))
print(part_two(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
