import unittest, task1


def task1_part2(data):
    lvl = 0
    for index, each in enumerate(data, start=1):
        lvl = task1.move_up_down(each, lvl)
        if lvl == -1:
            return index
    return None


class AllTestsTask1Part2(unittest.TestCase):

    def test1_task1_part2(self):
        actual = task1_part2(')')
        expected = 1
        self.assertEqual(actual, expected)

    def test2_task1_part2(self):
        actual = task1_part2('()())')
        expected = 5
        self.assertEqual(actual, expected)


path = 'inputs/task1.txt'
data = task1.read_data(path)
print(f'Position of the Basement is: {task1_part2(data)}')
