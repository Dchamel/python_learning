from itertools import permutations


def real(name):
    if len(name) < 5:
        raise ValueError('Too short string')

    y = 0
    for i in permutations(range(len(name)), 5):
        print(i)


# real('qwerqweqqq')

# --------------------------
from mock import patch
import itertools

name = ('qwerqe')

with patch('itertools.permutations') as perm_mock:
    perm_mock.return_value = range(1)
    real(name)
