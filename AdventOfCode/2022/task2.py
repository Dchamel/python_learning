import unittest
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


# tests
class AllTests2022Task2(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path

    # tests for part1
    def test01_read_data(self):
        expected = '5'
        actual = read_data(self.path)[12]
        self.assertEqual(expected, actual)


path = 'inputs/task2.txt'
data = read_data(path)

# opponent rock - A
X = 1
# opponent paper - B
Y = 2
# opponent scissors - C
Z = 3


def points(your_choice):
    if your_choice == 'X':
        your_points = 1
    elif your_choice == 'Y':
        your_points = 2
    elif your_choice == 'Y':
        your_points = 3
    return your_points


total_points = 0
for data_line in data.splitlines():
    oppo = data_line[0]
    you = data_line[2]
    if (oppo == 'A' and you == 'Z') or (oppo == 'B' and you == 'X') or (oppo == 'C' and you == 'Y'):
        total_points += 6 + points(you)
    elif oppo == you:
        total_points += 3 + points(you)
    else:
        total_points += points(you)

print(total_points)

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
