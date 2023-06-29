import unittest, string
from time import perf_counter

t1 = perf_counter()


def cells_in_range(s: str) -> list:
    final_list = []
    col_list = list(string.ascii_uppercase)
    cells_list = s.split(':')

    start_col = col_list.index(cells_list[0][0])
    end_col = col_list.index(cells_list[1][0])
    start_row = int(cells_list[0][1])
    end_row = int(cells_list[1][1])

    input_col_list = col_list[start_col:end_col + 1]

    for col in input_col_list:
        for row in range(start_row, end_row + 1):
            final_list += [col + str(row)]

    return final_list


# tests
class AllTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    # tests
    def test01_cells_in_range(self):
        expected = ["K1", "K2", "L1", "L2"]
        actual = cells_in_range(s="K1:L2")
        self.assertEqual(expected, actual)

    def test02_cells_in_range(self):
        expected = ["A1", "B1", "C1", "D1", "E1", "F1"]
        actual = cells_in_range(s="A1:F1")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
