import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Входные данные
X = np.array([[1], [2], [3], [4], [5]])  # Часы учёбы
y = np.array([2, 4, 6, 8, 10])  # Баллы за тест

# Создаем модель
model = LinearRegression()
model.fit(X, y)

# Делаем предсказание
y_pred = model.predict(X)

# Рисуем график
plt.scatter(X, y, color='blue', label='Исходные данные')
plt.plot(X, y_pred, color='red', label='Линия регрессии')
plt.xlabel('Часы учёбы')
plt.ylabel('Баллы')
plt.title('Простая линейная регрессия')
plt.legend()
plt.grid(True)
plt.show()
