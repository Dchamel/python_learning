# Импортируем нужные библиотеки
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Входные данные — площадь домов (X), и выходные — цены (y)
X = np.array([[40], [50], [60], [70], [80]])  # площадь домов
y = np.array([7_000_000, 8_000_000, 9_000_000, 10_000_000, 11_000_000])  # цены

# Создаем модель линейной регрессии
model = LinearRegression()

# Обучаем модель на данных
model.fit(X, y)

# Смотрим, какие коэффициенты нашла модель
print("Коэффициент (a):", model.coef_[0])
print("Свободный член (b):", model.intercept_)

# Предсказываем цену для дома площадью 65 м²
area_to_predict = np.array([[65]])
predicted_price = model.predict(area_to_predict)
print("Примерное значение цены для 65 м²:", predicted_price[0])

# Рисуем график
plt.scatter(X, y, color='blue', label='Реальные данные')
plt.plot(X, model.predict(X), color='red', label='Линия регрессии')
plt.xlabel('Площадь (м²)')
plt.ylabel('Цена (руб)')
plt.title('Линейная регрессия')
plt.legend()
plt.grid(True)
plt.show()
