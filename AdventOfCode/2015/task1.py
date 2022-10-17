import unittest

def readData(path):
    with open(path, 'r') as rawData:
        data = rawData.read()
    return data

def task1(data):
    lvl = 0
    for each in data:
        if each == '(':
            lvl += 1
        else:
            lvl -= 1
    return lvl

class AllTestsTask1(unittest.TestCase):
    def test_readData(self):
        actual = readData('inputs/task1.txt')[1]
        expected = '('
        self.assertEqual(actual, expected)

    def test_task1(self):
        actual = task1(')((')
        expected = 1
        self.assertEqual(actual, expected)

path = 'inputs/task1.txt'
data = readData(path)
print(task1(data))