import unittest, re
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.read()


def check_3_vowels(string4check: str) -> bool:
    '''Check for 3 vowels. Out - true/false'''
    VOWELS = 'aeiou'
    count = 0
    for letter in VOWELS:
        if letter in string4check:
            letter_quantity = string4check.count(letter)
            if letter_quantity > 1:
                count += letter_quantity
            else:
                count += 1
    return count >= 3


def check_double_letter(string4check):
    letter_before = ''
    for letter in string4check:
        if letter_before == letter:
            return True
        letter_before = letter
    return False


def check_4_forbidden_strings(string4check):
    forbidden_strings = ['ab', 'cd', 'pq', 'xy']
    for forbidden_string in forbidden_strings:
        if forbidden_string in string4check:
            return False
    else:
        return True


def nice_string(data):
    index = 0
    for string4check in data.splitlines():
        check1 = check_3_vowels(string4check)
        check2 = check_double_letter(string4check)
        check3 = check_4_forbidden_strings(string4check)
        if check1 and check2 and check3:
            index += 1
    return index


# part2
def check_4_2letters_not_overlapping(string4check):
    for index, letter in enumerate(string4check, start=0):
        if string4check.count(letter) >= 2:

            try:
                letter_from_string4check = string4check[index + 1]
            except:
                return False

            check_substr = letter + letter_from_string4check

            final_check = string4check.count(check_substr)
            if final_check >= 2:
                return True
    return False


def check_double_letter_between_letter(string4check):
    for letter in string4check:
        if string4check.count(letter) >= 2:
            positions = []
            for i in re.finditer(letter, string4check):
                positions.append(i.start())
            for i in range(1, len(positions)):
                if positions[i] - positions[i - 1] == 2:
                    return True
    return False


def nice_string2(data):
    index = 0
    for string4check in data.splitlines():
        check1 = check_4_2letters_not_overlapping(string4check)
        check2 = check_double_letter_between_letter(string4check)
        if check1 and check2:
            index += 1
    return index


# tests
class AllTestsTask5(unittest.TestCase):

    # tests for part1
    def test01_read_data(self):
        expected = 'u'
        actual = read_data('inputs/task5.txt')[4]
        self.assertEqual(expected, actual)

    def test02_check_3_vowels(self):
        actual = check_3_vowels('ugknbfddgicrmopn')
        self.assertTrue(actual)

    def test03_check_double_letter(self):
        actual = check_double_letter('ugknbfddgicrmopn')
        self.assertTrue(actual)

    def test04_heck_string_4_twoletters(self):
        actual = check_double_letter('ugknbfddgicrmopn')
        self.assertTrue(actual)

    def test05_nice_string1(self):
        expected = 1
        actual = nice_string('ugknbfddgicrmopn')
        self.assertEqual(expected, actual)

    def test06_nice_string2(self):
        expected = 1
        actual = nice_string('aaa')
        self.assertEqual(expected, actual)

    def test07_nice_string3(self):
        expected = 0
        actual = nice_string('jchzalrnumimnmhp')
        self.assertEqual(expected, actual)

    def test08_nice_string4(self):
        expected = 0
        actual = nice_string('haegwjzuvuyypxyu')
        self.assertEqual(expected, actual)

    def test09_nice_string5(self):
        expected = 0
        actual = nice_string('dvszwmarrgswjxmb')
        self.assertEqual(expected, actual)

    def test10_nice_string2_1(self):
        expected = 1
        actual = nice_string2('qjhvhtzxzqqjkmpb')
        self.assertEqual(expected, actual)

    def test11_nice_string2_2(self):
        expected = 1
        actual = nice_string2('xxyxx')
        self.assertEqual(expected, actual)

    def test12_nice_string2_3(self):
        expected = 0
        actual = nice_string2('uurcxstgmygtbstg')
        self.assertEqual(expected, actual)

    def test13_nice_string2_4(self):
        expected = 0
        actual = nice_string2('ieodomkazucvgmuy')
        self.assertEqual(expected, actual)


path = 'inputs/task5.txt'
data = read_data(path)
print(f'Part1 result: {nice_string(data)}')
print(f'Part2 result: {nice_string2(data)}')

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
