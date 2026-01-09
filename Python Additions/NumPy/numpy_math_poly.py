import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt  # всё равно нужен

df = pd.DataFrame({
    'month': np.arange(1, 13),
    'volume': [102, 105, 110, 112, 118, 125, 130, 138, 142, 150, 155, 160]
})

# Подгонка полинома
poly = np.poly1d(np.polyfit(df['month'], df['volume'], deg=2))
x_fit = np.linspace(df['month'].min(), df['month'].max(), 200)
y_fit = poly(x_fit)

# Визуализация
sns.scatterplot(data=df, x='month', y='volume')
plt.plot(x_fit, y_fit, color='red', label='Тренд (полином)')
plt.legend()
plt.show()
