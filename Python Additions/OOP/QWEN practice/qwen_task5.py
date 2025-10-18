# Расширь классы Point и ColorPoint, чтобы они поддерживали удобные операции через магические методы.
#
# Добавь в класс Point следующие методы:
# __eq__(self, other)
# — Две точки равны, если у них одинаковые координаты x и y.
# — Должно работать при сравнении с другим Point или ColorPoint.
# __add__(self, other)
# — Сложение двух точек: создаётся новая точка с координатами (x1 + x2, y1 + y2).
# — Если складывается с ColorPoint, желательно сохранить тип (см. ниже).
# __repr__(self)
# — Возвращает строку, удобную для отладки и воссоздания объекта, например:
# "Point(1, 2)" или "ColorPoint(3, 4, 'красный')".
# Добавь в класс ColorPoint:
# Переопределение __repr__
# Переопределение __add__, чтобы при сложении двух цветных точек результат тоже был ColorPoint (и, например, сохранял цвет левой точки)
# Убедись, что __eq__ работает корректно (наследуется или переопределяется)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка({self.x}, {self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and isinstance(other, Point):
            return True
        elif self.x == other.x and self.y == other.y and not isinstance(other, Point):
            return False

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5


class ColorPoint(Point):
    """Класс точек с цветом"""

    def __init__(self, x=0, y=0, color='Без цвета'):
        super().__init__(x, y)
        self.color = color

    def __str__(self):
        return f'Точка({self.x}, {self.y}) цвет: {self.color}'

    def __add__(self, other):
        if isinstance(other, ColorPoint):
            return Point(self.x + other.x, self.y + other.y)


if __name__ == '__main__':
    # p1 = ColorPoint(1, 2)
    # p2 = ColorPoint(3, 4)
    # cp = ColorPoint(5, 6)

    p1 = Point(1, 2)
    p2 = Point(1, 2)
    cp = ColorPoint(1, 2, "синий")

    print(p1 == p2)  # True
    print(p1 == cp)  # True (по координатам!)
    print(p1 + p2)  # Точка(2, 4)
    print(cp + p1)  # Точка(2, 4) цвет: синий
    print(repr(cp))  # ColorPoint(1, 2, 'синий')
