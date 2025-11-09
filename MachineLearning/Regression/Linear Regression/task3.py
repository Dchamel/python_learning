from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Искусственные данные
np.random.seed(42)
area = np.random.randint(50, 200, 100)  # Площадь домов
rooms = np.random.randint(1, 6, 100)  # Количество комнат
price = area * 100 + rooms * 5000 + np.random.normal(0, 5000, 100)  # Цена с шумом

# Объединяем признаки в матрицу
X = np.column_stack((area, rooms))
y = price

# Разделяем данные
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучаем модель
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказываем
y_pred = model.predict(X_test)

# Строим график (только площадь против цены для наглядности)
plt.scatter(X_test[:, 0], y_test, color='blue', label='Реальные цены')
plt.scatter(X_test[:, 0], y_pred, color='red', label='Предсказанные цены')
plt.xlabel('Площадь')
plt.ylabel('Цена')
plt.title('Множественная регрессия (площадь vs цена)')
plt.legend()
plt.grid(True)
plt.show()
