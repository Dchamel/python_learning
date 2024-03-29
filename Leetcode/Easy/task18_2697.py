import unittest
from time import perf_counter

t1 = perf_counter()


def sm_palindrome(s: str) -> str:
    def get_half_str_len(s: str):
        index = 0
        if len(s) % 2 == 0:
            index = int(len(s) / 2)
        else:
            index = len(s) / 2

        return index

    index = get_half_str_len(s)

    if type(index) == float:
        index = int(index)
        str1 = s[0:index]
        str2 = s[-1:index:-1]
        step = 0
        for i in range(index):
            if str1[i] == str2[i]:
                continue
            else:
                if str1[i] >= str2[i]:
                    str1 = list(str1)
                    str1[i] = str2[i]
                    str1 = ''.join(str1)
                    step += 1
                else:
                    str2 = list(str2)
                    str2[i] = str1[i]
                    str2 = ''.join(str2)
                    step += 1

        if str1 >= str2:
            str2 = ''.join(str1)[::-1]
            palindrome_str = str1 + s[index] + str2
        else:
            str1 = ''.join(str2)[::-1]
            palindrome_str = str2 + s[index] + str1

    else:
        str1 = s[0:index]
        str2 = s[-1:index - 1:-1]
        step = 0
        for i in range(index):
            if str1[i] == str2[i]:
                continue
            else:
                if str1[i] >= str2[i]:
                    str1 = list(str1)
                    str1[i] = str2[i]
                    str1 = ''.join(str1)
                    step += 1
                else:
                    str2 = list(str2)
                    str2[i] = str1[i]
                    str2 = ''.join(str2)
                    step += 1

        if str1 <= str2:
            str2 = ''.join(str1)[::-1]
            palindrome_str = str1 + str2
        else:
            str1 = ''.join(str2)[::-1]
            palindrome_str = str2 + str1

    return palindrome_str


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_sm_palindrome(self):
        expected = "efcfe"
        actual = sm_palindrome(s="egcfe")
        self.assertEqual(expected, actual)

    def test02_sm_palindrome(self):
        expected = "abba"
        actual = sm_palindrome(s="abcd")
        self.assertEqual(expected, actual)

    def test03_sm_palindrome(self):
        expected = "neven"
        actual = sm_palindrome(s="seven")
        self.assertEqual(expected, actual)

    def test04_sm_palindrome(self):
        expected = "caac"
        actual = sm_palindrome(s="cauc")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
