import unittest
from time import perf_counter

t1 = perf_counter()


def goal_parser(command: str):
    command = command.replace('()', 'o')
    command = command.replace('(al)', 'al')
    return command


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_goal_parser(self):
        expected = "Goal"
        actual = goal_parser("G()(al)")
        self.assertEqual(expected, actual)

    def test02_goal_parser(self):
        expected = "Gooooal"
        actual = goal_parser("G()()()()(al)")
        self.assertEqual(expected, actual)

    def test03_goal_parser(self):
        expected = "alGalooG"
        actual = goal_parser("(al)G(al)()()G")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
