# Задача 2: Класс "Банковский счёт" (BankAccount)
# Создай класс BankAccount, представляющий банковский счёт. У него должны быть:
#
# Приватный атрибут __balance (для хранения баланса)
# Атрибут owner — имя владельца
# Методы:
#
# __init__(self, owner, initial_balance=0)
# deposit(self, amount) — пополнение счёта
# withdraw(self, amount) — снятие денег; если средств недостаточно, вывести сообщение
# get_balance(self) — возвращает текущий баланс
# __str__(self) — например: "Счёт [Имя]: баланс 1000 руб."
# ⚠️ Не забудь проверять, что сумма положительная, и при снятии — что хватает денег.

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self.__balance = initial_balance

    def __str__(self):
        return f"Счёт {self.owner}: баланс {self.__balance} руб."

    def deposit(self, amount):
        if amount < 0:
            print("Пополнение не может быть отрицательным")с
            return
        self.__balance += amount
        print(f"Пополнено на {amount} руб. Текущий баланс: {self.__balance} руб.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("There is no such money")
            return
        elif amount == 0:
            print("Amount cannot be 0")
            return
        self.__balance -= amount
        print(f"Снято {amount} руб. Текущий баланс: {self.__balance} руб.")

    def get_balance(self):
        return self.__balance
