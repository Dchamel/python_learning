import unittest, hashlib
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        data = rawData.read()
    return data


def md5hex(data) -> str:
    return hashlib.md5(data.encode()).hexdigest()


def find_5zeroes(data):
    i = 0
    new_string_md5 = ''
    while not new_string_md5.startswith('00000'):
        i += 1
        new_string = data + str(i)
        new_string_md5 = md5hex(new_string)
    return i


def find_6zeroes(data):
    i = 0
    new_string_md5 = ''
    while not new_string_md5.startswith('000000'):
        i += 1
        new_string = data + str(i)
        new_string_md5 = md5hex(new_string)
    return i


# tests
class AllTestsTask4(unittest.TestCase):

    # tests for part1
    def test1_read_data(self):
        expected = 'z'
        actual = read_data('inputs/task4.txt')[3]
        self.assertEqual(expected, actual)

    def test2_md5hex(self):
        expected = '96f0f08c0188ba04898ce8cc465c19c4'
        actual = md5hex('asdqwe')
        self.assertEqual(expected, actual)

    def test5_find_5zeroes_1(self):
        expected = 609043
        actual = find_5zeroes('abcdef')
        self.assertEqual(expected, actual)

    def test6_find_5zeroes_2(self):
        expected = 1048970
        actual = find_5zeroes('pqrstuv')
        self.assertEqual(expected, actual)


path = 'inputs/task4.txt'
data = read_data(path)
print(find_5zeroes(data))
print(find_6zeroes(data))

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
