import unittest
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def points(your_choice):
    if your_choice == 'X':
        your_points = 1
    elif your_choice == 'Y':
        your_points = 2
    elif your_choice == 'Z':
        your_points = 3

    return your_points


def first_part(data):
    total_points = 0
    for data_line in data.splitlines():
        oppo = data_line[0]
        you = data_line[2]
        if (oppo == 'A' and you == 'Y') or (oppo == 'B' and you == 'Z') or (oppo == 'C' and you == 'X'):
            total_points += 6 + points(you)
        elif (oppo == 'A' and you == 'X') or (oppo == 'B' and you == 'Y') or (oppo == 'C' and you == 'Z'):
            total_points += 3 + points(you)
        else:
            total_points += points(you)
    return total_points


# tests
class AllTests2022Task2(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path
        self.data = 'A Y\nB X\nC Z'

    def test01_read_data(self):
        expected = 'X'
        actual = read_data(self.path)[2]
        self.assertEqual(expected, actual)

    def test02_first_part1(self):
        expected = 15
        actual = first_part(self.data)
        self.assertEqual(expected, actual)


path = 'inputs/task2.txt'
data = read_data(path)

print(first_part(data))


def second_part(data):
    total_points = 0
    for data_line in data.splitlines():
        oppo = data_line[0]
        you = data_line[2]
        if you == 'X':
            if oppo == 'A':
                total_points += 3
            elif oppo == 'B':
                total_points += 1
            elif oppo == 'C':
                total_points += 2

        elif you == 'Z':
            if oppo == 'A':
                total_points += 8
            elif oppo == 'B':
                total_points += 9
            elif oppo == 'C':
                total_points += 7

        elif you == 'Y':
            if oppo == 'A':
                total_points += 4
            elif oppo == 'B':
                total_points += 5
            elif oppo == 'C':
                total_points += 6

    return total_points


print(second_part(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
