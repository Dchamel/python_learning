import unittest
from time import perf_counter

t1 = perf_counter()

"""
1812

You are given {coordinates}, a string that represents the 
coordinates of a square of the chessboard. Below is a 
chessboard for your reference.
Return {true} if the square is white, and {false} if the 
square is black.
The coordinate will always represent a valid chessboard square. 
The coordinate will always have the letter first, 
and the number second.
Constraints:
- {coordinates.length == 2}
- {'a' <= coordinates[0] <= 'h'}
- {'1' <= coordinates[1] <= '8'}
"""


def squareIsWhite(coordinates: str) -> bool:
    """Takes coords for generated regular chessboard(by this func below)
    and return 'true' if square is White and 'false' if Black"""
    board = []
    x_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for x in range(8):
        xx = []
        for y in range(8):
            if (x + y) % 2 == 0:
                xx.append('black')
            else:
                xx.append('white')
        board.append(xx)
    index_letter = x_letters.index(coordinates[0])
    if board[index_letter][int(coordinates[1]) - 1] == 'white':
        return True
    else:
        return False


print(squareIsWhite(coordinates="h3"))


# tests
class AllTests(unittest.TestCase):

    def test00_squareIsWhite(self):
        expected = False
        actual = squareIsWhite(coordinates="a1")
        self.assertEqual(expected, actual)

    def test01_squareIsWhite(self):
        expected = True
        actual = squareIsWhite(coordinates="h3")
        self.assertEqual(expected, actual)

    def test02_squareIsWhite(self):
        expected = False
        actual = squareIsWhite(coordinates="c7")
        self.assertEqual(expected, actual)


t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
