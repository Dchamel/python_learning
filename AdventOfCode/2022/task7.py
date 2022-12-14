import unittest, re
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.readlines()


# tests - not implemented
class AllTests2022Task2(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path
        self.data = ''

    def test01_read_data(self):
        expected = 's'
        actual = read_data(self.path)[3]
        self.assertEqual(expected, actual)


path = 'inputs/task7.txt'
data = read_data(path)

# One of the ideas was use a regexp but after some thoughts i decided not to do this
# q = re.findall('[^$.*ls\n](?:.*)[^\n$.*ls]', data)

path_list = []
for data_line in data:
    match data_line.strip():
        case '$ cd /' as indata:
            path_list.append('/')
        case '$ ls':
            continue
        case 'dir' if 'dir' in data_line:
            dir_name = data_line.replace('dir ')
            path_list.append(path_list[-1] + dir_name)

print([path for path in path_list])

# print(re.findall('[$ cd ]\/\n', '$ cd /\n'))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
