import unittest
from time import perf_counter

t1 = perf_counter()


def countAsterisks(s: str) -> int:
    list_map = []
    for index, symb in enumerate(s):
        if symb == '|':
            list_map.append(index)
        else:
            continue
    if 0 not in list_map:
        list_map.insert(0, 0)
    if s[0] == '|':
        list_map.insert(0, 0)
    w = []
    print(list_map)
    for i in range(0, len(list_map), 2):
        try:
            q = s[list_map[i]:list_map[i + 1]]
            print(q)
            w.append([each for each in q if each == '*'].count('*'))
        except:
            q = s[list_map[i]:]
            w.append([each for each in q if each == '*'].count('*'))

    return sum(w)


print(countAsterisks(s="*||||**||*||**|**||*|||**"))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_countAsterisks(self):
        expected = 2
        actual = countAsterisks(s="l|*e*et|c**o|*de|")
        self.assertEqual(expected, actual)

    def test02_countAsterisks(self):
        expected = 0
        actual = countAsterisks(s="iamprogrammer")
        self.assertEqual(expected, actual)

    def test03_countAsterisks(self):
        expected = 5
        actual = countAsterisks(s="yo|uar|e**|b|e***au|tifu|l")
        self.assertEqual(expected, actual)

    def test04_countAsterisks(self):
        expected = 6
        actual = countAsterisks(s="|**|*|*|**||***||")
        self.assertEqual(expected, actual)

    def test05_countAsterisks(self):
        expected = 8
        actual = countAsterisks(s="*||||**||*||**|**||*|||**")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
