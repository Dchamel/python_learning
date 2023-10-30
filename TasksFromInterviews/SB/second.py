# Задание №2 (Pandas)
#
# Дан датафрейм Pandas Sales, в котором хранятся продажи
# и возвраты: Shop   Employee   Type   Sum
#
# Описание полей:
#
#     Shop - название магазина
#     Employee - имя сотрудника
#     Type - тип транзакции (продажа - 1, возврат - 2)
#     Sum - сумма транзакции
#
# Руководитель просит подбить итоги в разрезе каждого
# сотрудника в каждом отдельном магазине:
#
#     Сколько возвратов и сколько продаж было?
#     Какая сумма продаж и возвратов?
#     Какая средняя сумма продажи и возврата?
#
# Результат необходимо оформить в виде датафрейма следующего вида:
# Shop   Employee   Type   Amount   Sum   Avg
#
# Примечание: После всех преобразований все поля
# (Shop, Employee, Type, Amount, Sum, Avg) должны быть столбцами
# итогового датафрейма df. Другими словами, например,
# конструкция df['Shop'] не должна выдавать ошибку.


import pandas as pd
import numpy as np

# input data
df = pd.DataFrame(data=[
    {'Shop': "Yakimanka", 'Employee': "Anna", 'Type': 1, 'Sum': 528},
    {'Shop': "Yakimanka", 'Employee': "Fedor", 'Type': 2, 'Sum': 632},
    {'Shop': "Butovo", 'Employee': "Peter", 'Type': 1, 'Sum': 115},
    {'Shop': "Yakimanka", 'Employee': "Anna", 'Type': 1, 'Sum': 1024},
    {'Shop': "Butovo", 'Employee': "Peter", 'Type': 1, 'Sum': 1754},
    {'Shop': "Butovo", 'Employee': "Peter", 'Type': 1, 'Sum': 111},
    {'Shop': "Kamenka", 'Employee': "Max", 'Type': 1, 'Sum': 499},
    {'Shop': "Kamenka", 'Employee': "Max", 'Type': 2, 'Sum': 23},
    {'Shop': "Butovo", 'Employee': "Jugen", 'Type': 1, 'Sum': 214},
    {'Shop': "Kamenka", 'Employee': "Max", 'Type': 1, 'Sum': 964},
    {'Shop': "Yakimanka", 'Employee': "Fedor", 'Type': 2, 'Sum': 100},
    {'Shop': "Butovo", 'Employee': "Jugen", 'Type': 1, 'Sum': 10000}
])

df2 = pd.DataFrame()

# First Attempt
# df2['Amount'] = df.groupby(['Employee', 'Shop', 'Type'])['Sum'].size()
# df2['Sum'] = df.groupby(['Employee', 'Shop', 'Type'])['Sum'].sum()
# df2['Avg'] = df.groupby(['Employee', 'Shop', 'Type'])['Sum'].mean()
# df2 = df2.reset_index()
# df = df2[['Shop', 'Employee', 'Type', 'Amount', 'Sum', 'Avg']]
# print(df.columns)
# print(df)

# Second Attempt
df2[['Amount', 'Sum', 'Avg']] = df.groupby(['Employee', 'Shop', 'Type'], as_index=True).agg(
    {'Sum': ['size', 'sum', 'mean']})
df = df2.reset_index()
print(df)
