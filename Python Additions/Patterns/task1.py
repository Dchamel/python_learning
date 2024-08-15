# Task1
# Реализуйте шаблон-класс в котором наследование используется для разделения
# ответственности между классами, чтобы разделять абстракцию и реализацию так,
# чтобы они могли изменяться независимо (шаблон 'Мост')

class DrawingMethod:
    def drawPoint(self, x, y, id):
        pass


class Shape:
    def draw(self):
        pass

    def getAttr(self):
        pass


def main():
    shapes = [
        Point(1, 2, 1001, DrawingMethod1()),
        Point(5, 7, 1002, DrawingMethod2())
    ]

    for shape in shapes:
        shape.getAttr()
        shape.draw()
