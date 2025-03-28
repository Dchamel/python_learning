# Дана строка, состоящая из букв 'X', 'Y' и 'O'.
# Необходимо найти кратчайшее расстояние между буквами 'X' и 'Y',
# либо вывести 0, если 'X' либо 'Y' отсутствуют.

# "YY" -> 0
# "XX" -> 0
# "XY" -> 1
# "YOX" -> 2
# "OOOXOOYOXO" -> 2
# "OOOXXOY"-> 2

def distance(input: str) -> int:
    last_x = None
    last_y = None
    min_distance = None
    for i, letter in enumerate(input):
        if letter == 'X':
            if last_y is not None and (min_distance is None or i - last_y < min_distance):
                min_distance = i - last_y
            last_x = i
        elif letter == 'Y':
            if last_x is not None and (min_distance is None or i - last_x < min_distance):
                min_distance = i - last_x
            last_y = i

    return min_distance or 0

print(distance('OOOXOOYOX'))