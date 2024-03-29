# Задание №1
# (Pure Python)

# Заполнить одномерный массив A длиной N случайными вещественными
# числами от 0 до 10 (значение N вводится с клавиатуры).
# Сформировать новый массив B, в котором значение B[i]
# равно количеству элементов массива A, удовлетворяющих
# неравенству i <= A[j] < (i+1) для i от 0 до 9.
# Массив A «в столбик», а массив B – «в строку» вывести на экран.

from random import uniform
import pandas

# part1
n = int(input())
a = [round(uniform(0.0, 11.0), 2) for _ in range(n)]
print(a)

# rotating into column
a1 = pandas.DataFrame(a)
a1.T
print(a1)

# part2
b = []
for i in range(10):
    q = 0
    for j in a1[0]:
        if j >= i and j < i + 1:
            q += 1
    b.append(q)
print(b)
