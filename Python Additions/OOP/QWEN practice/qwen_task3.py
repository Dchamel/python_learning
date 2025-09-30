# Задача 3 (немного сложнее): Класс "Точка" (Point)
# Создай класс Point, представляющий точку в двумерном пространстве.
#
# Атрибуты: x, y
# Методы:
# __init__(self, x=0, y=0)
# move(self, dx, dy) — перемещает точку на dx по X и dy по Y
# distance_to(self, other_point) — возвращает расстояние до другой точки (по формуле: √((x₂-x₁)² + (y₂-y₁)²))
# __str__(self) — например: "Точка(3, 4)"
# 💡 Подсказка: для корня используй math.sqrt() или ** 0.5.

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка({self.x}, {self.y})'

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5
