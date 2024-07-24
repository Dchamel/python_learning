from time import perf_counter


def working_time_prec(prec=2):
    def working_time(func):
        def wrapper():
            t1 = perf_counter()
            func()
            t2 = perf_counter()
            print(f'Working time: {t2 - t1:.{prec}f} seconds')
            return func

        return wrapper

    return working_time


# Here I only notice that we have this algorithms
# Изучить. Проверить сочетание со скользящими средними и как это использовать для предсказаний.
def linear_regression():
    pass


def logistic_regression():
    pass


def decision_tree():
    pass


def random_forest():
    pass


def knn_classifier():
    """
    Алгоритм k-ближайших соседей. Алгоритм классификации и регрессииб
    использует информацию о ближайших соседях для принятия решений.
    """
    pass


def svm_classifier():
    """
    Support Vector Machines (SVM)

    """
    pass


def naive_bayes_classifier():
    pass


@working_time_prec()
def main():
    pass


if __name__ == '__main__':
    main()
