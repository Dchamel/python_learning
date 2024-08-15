# Task 2
# Есть система "гараж"б у него есть 3 объекта-handlers, на вход им подается объект
# "автомобиль" с тремя атрибутами (масло, топливо, пробег). Каждый из трех объектов
# обрабатывает входную информацию определеного типа и производит отдельное действие:

# - если топлива меньше 10, сообщает, что добавил топлива;
# - если пробег более 10000, сообщает, что сделал тех. осмотр;
# - если масло меньше 10, сообщает, что добавил масла.

# Реализуйте три таких объекта-handlers

handlers = []


class Car:
    def __init__(self):
        self.name = None
        self.km = 11100
        self.fuel = 5
        self.oil = 5

    def car_handler(func):
        handlers.append(func)
        return func


class Garage:
    def __init__(self, handlers=None):
        self.handlers = handlers or []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def handle_car(self, car):
        for handler in self.handlers:
            handler(car)


garage = Garage(handlers)
car = Car()
garage.handle_car(car)
