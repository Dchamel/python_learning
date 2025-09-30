# Задача 1: Класс "Книга" (Book)
# Создай класс Book, который имеет следующие атрибуты:
#
# title — название книги
# author — автор
# pages — количество страниц
# is_read — булево значение (по умолчанию False)
# Методы:
#
# __init__(self, title, author, pages) — конструктор
# mark_as_read(self) — метод, который помечает книгу как прочитанную и выводит сообщение: "Вы прочитали 'Название' от автора Автор"
# __str__(self) — строковое представление книги, например:
# "Книга: 'Война и мир' — Лев Толстой, 1225 стр."
# 💡 Подсказка: используй f-строки.

class Book:
    '''task1'''

    def __init__(self,
                 title,
                 author,
                 pages,
                 is_read=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read

    def __str__(self):
        return f'Книга: {self.title} - {self.author}, {self.pages} стр.'

    def mark_as_read(self) -> str:
        self.is_read = True

        return f"Вы прочитали {self.title} от автора {self.author}"
