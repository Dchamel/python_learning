import time, unittest
from time import perf_counter
from typing import Callable


def working_time(func) -> Callable:
    '''Decorator for counting working time'''

    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        time.sleep(1)
        content = func(*args, **kwargs)
        t2 = perf_counter()
        print(f'{t2 - t1:.5f} sec')
        return content

    return wrapper


def longestCommonPrefix(strs: list[str]) -> str:
    '''Returns the longest common prefix from strings in list'''
    prefix = ''

    def recur_check_4_letters(strs: list[str]):
        '''Recursion for first lettres'''
        for elem in strs:
            if elem[0]
        return recur_check_4_letters(str[1:])

    return '1'


@working_time
def main():
    strs = ["flower", "flow", "flight"]
    return longestCommonPrefix(strs)


if __name__ == '__main__':
    main()


# tests
class AllTestsEasy13(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_longestCommonPrefix(self):
        pass
        # expected = "fl"
        # actual = longestCommonPrefix(["flower","flow","flight"])
        # self.assertEqual(expected, actual)

    def test02_longestCommonPrefix(self):
        pass
        # expected = ""
        # actual = longestCommonPrefix(["dog","racecar","car"])
        # self.assertEqual(expected, actual)
