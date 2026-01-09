from MyProjects.MyModules.time_additional import working_time_prec
import numpy as np
import matplotlib.pyplot as plt
from numpy import poly1d


def basic_funcs_from_book():
    """Just some basic functions from the Book"""

    np.array([1, 2, 3])  # Массив из списка
    np.zeros(3)  # Массив нулей
    np.ones(3)  # Массив единиц
    np.empty(3)  # Массив произвольных данных
    np.arange(3)  # Массив из диапазона чисел
    np.arange(0, 12, 3)  # Массив из диапазона чисел
    np.linspace(0, 21, 7)  # Массив интервалов


def basic_funcs_from_array():
    """Array functions from the book"""

    arr = np.arange(20)
    print(arr)
    print(arr.dtype)
    print(arr.size)
    print(arr.nbytes)
    print(arr.shape)
    print(arr.ndim)
    print(type(arr))


def basic_funcs_of_create_array():
    """Create array functions from the book"""

    list_o_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    arr = np.array(list_o_lists)
    print(arr)
    print(arr.shape)
    print(arr.ndim)
    img = np.random.rand(2, 3, 3)
    shape = img.shape
    dtype = img.dtype
    ndim = img.ndim
    x = np.array([[[1, 2, 3]]])  # shape: (1, 1, 3)
    x = x.squeeze()  # shape: (3,)
    # x = x.squeeze(axis=0)  # shape: (1, 3)
    arr = np.arange(20)
    arr = arr.reshape(2, 2, -1)
    print(arr)


def using_zip_with_matplotlib():
    """Using zip with matplotlib"""

    categories = ['A', 'B', 'C', 'D']
    values = [10, 25, 15, 30]
    colors = ['red', 'blue', 'green', 'orange']

    plt.bar(categories, values, color=colors)

    # Добавим подписи значений над столбцами
    for x, y, c in zip(categories, values, colors):
        plt.text(x, y + 0.5, str(y), ha='center', color=c, weight='bold')

    plt.show()


def matrix_operations():
    """Matrix operations"""

    A1 = np.arange(9).reshape(3, 3)
    # A1 = A1.T
    A2 = np.ones(9).reshape(3, 3)
    A12 = A1 @ A2
    A121 = A1.dot(A2)


def array_broadcasting():
    """Array Broadcasting"""

    darr = np.arange(9, dtype=np.int8)
    print(darr)
    darr = darr.reshape(3, -1)
    print(darr)
    darr_ones = np.ones((3, 3), dtype=np.int8)
    print(darr_ones)
    darr_summ = darr + darr_ones
    print(darr_summ)
    print(darr + 1)


def numpy_math():
    """Numpy Math"""

    months = np.arange(1, 13)  # 1–12
    volume = np.array([102, 105, 110, 112, 118, 125, 130, 138, 142, 150, 155, 160])

    # Подбираем полином 2-й степени
    coeffs = np.polyfit(months, volume, deg=2)
    poly = np.poly1d(coeffs)

    # Визуализация
    plt.scatter(months, volume, label='Данные')
    plt.plot(months, poly(months), color='red', label='Тренд (полином)')
    plt.legend();
    plt.show()


@working_time_prec(6)
def main():
    """Main class for NumPy calculations"""

    # basic_funcs_from_book()
    # basic_funcs_from_array()
    # basic_funcs_of_create_array()
    # using_zip_with_matplotlib()
    # matrix_operations()
    # array_broadcasting()
    numpy_math()


if __name__ == '__main__':
    main()
