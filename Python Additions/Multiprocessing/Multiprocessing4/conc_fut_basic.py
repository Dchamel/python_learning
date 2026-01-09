from concurrent.futures import ProcessPoolExecutor


def square(x):
    return x * x


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        results = executor.map(square, [1, 2, 3, 4])
        print(list(results))  # [1, 4, 9, 16]
