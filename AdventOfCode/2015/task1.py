import unittest


def read_data(path):
    with open(path, 'r') as rawData:
        data = rawData.read()
    return data


def move_up_down(each, lvl):
    if each == '(':
        lvl += 1
    else:
        lvl -= 1
    return lvl


def task1(data):
    lvl = 0
    for each in data:
        lvl = move_up_down(each, lvl)
    return lvl


class AllTestsTask1(unittest.TestCase):
    def test1_read_data(self):
        actual = read_data('inputs/task1.txt')[1]
        expected = '('
        self.assertEqual(actual, expected)

    def test2_task1(self):
        actual = task1(')((')
        expected = 1
        self.assertEqual(actual, expected)

    def test3_task1(self):
        actual = [task1('(())'), task1('()()')]
        expected = 0
        self.assertIn(expected, actual)

    def test4_task1(self):
        actual = [task1('((('), task1('(()(()(')]
        expected = 3
        self.assertIn(expected, actual)

    def test5_task1(self):
        actual = task1('))(((((')
        expected = 3
        self.assertEqual(actual, expected)

    def test6_task1(self):
        actual = [task1('())'), task1('))(')]
        expected = -1
        self.assertIn(expected, actual)

    def test7_task1(self):
        actual = [task1(')))'), task1(')())())')]
        expected = -3
        self.assertIn(expected, actual)


if __name__ == '__main__':
    path = 'inputs/task1.txt'
    data = read_data(path)
    print(task1(data))
