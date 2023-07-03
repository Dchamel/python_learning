import unittest, string
from time import perf_counter

t1 = perf_counter()


def message_decoder(key: str, message: str) -> str:
    final_message = ''
    reg_alphabet = list(string.ascii_lowercase)
    key = key.replace(' ', '')
    key_uniq = []
    [key_uniq.append(i) for i in key if i not in key_uniq]
    code_alphabet_dict = dict(zip(key_uniq, reg_alphabet))
    for letter in message:
        if letter == ' ':
            final_message += ' '
        else:
            final_message += code_alphabet_dict[letter]

    return final_message


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_message_decoder(self):
        expected = "this is a secret"
        actual = message_decoder(key="the quick brown fox jumps over the lazy dog", message="vkbs bs t suepuv")
        self.assertEqual(expected, actual)

    def test02_message_decoder(self):
        expected = "the five boxing wizards jump quickly"
        actual = message_decoder(key="eljuxhpwnyrdgtqkviszcfmabo", message="zwx hnfx lqantp mnoeius ycgk vcnjrdb")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
