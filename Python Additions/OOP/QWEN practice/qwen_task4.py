# Задача: ColorPoint — точка с цветом
# Создай класс ColorPoint, который:
#
# наследуется от Point
# добавляет атрибут color (например, "красный")
# переопределяет метод __str__, чтобы выводилось:
# "Точка(2, 3) цвет: красный"
# ⚠️ При этом должен работать move() и distance_to() — они унаследуются!

from qwen_task3 import Point


class ColorPoint(Point):
    """Класс точек с цветом"""

    def __init__(self, x=0, y=0, color='Без цвета'):
        super().__init__(x, y)
        self.color = color

    def __str__(self):
        return f'Точка({self.x}, {self.y}) цвет: {self.color}'
