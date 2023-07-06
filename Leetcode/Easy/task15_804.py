import unittest, string
from time import perf_counter

t1 = perf_counter()


def morse_code_uniq(words: list) -> int:
    morse_alphabet_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                           "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alphabet = list(string.ascii_lowercase)
    morse_alphabet_dict = dict(zip(alphabet, morse_alphabet_list))
    morse_input_list = []
    for letters in words:
        one_morse_word = ''.join(list(map(lambda l: morse_alphabet_dict[l], [letter for letter in letters])))
        morse_input_list.append(one_morse_word)
    return len(set(morse_input_list))


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_morse_code_uniq(self):
        expected = 2
        actual = morse_code_uniq(words=["gin", "zen", "gig", "msg"])
        self.assertEqual(expected, actual)

    def test02_morse_code_uniq(self):
        expected = 1
        actual = morse_code_uniq(words=["a"])
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
