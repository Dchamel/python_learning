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


def lossless_gigachat(data):
    """
    Realization of algorithm (Huffman's algorithm) by Gigachat
    p.s. it did it wrong !
    """

    frequency_dict = {}

    # counting frequency of each symbol
    for symbol in data:
        if symbol not in frequency_dict:
            frequency_dict[symbol] = 1
        else:
            frequency_dict[symbol] += 1

    max_frequency = max(frequency_dict.values())
    max_symbol = None

    for symbol, frequency in frequency_dict.items():
        if frequency == max_frequency:
            max_symbol = symbol

    compressed_data = []
    current_frequency = 0

    for symbol in data:
        if symbol == max_symbol:
            current_frequency += 1
        else:
            compressed_data.append((max_frequency, current_frequency))
            current_frequency = 0
            max_frequency = max_frequency + 1
            max_symbol = symbol

    compressed_data.append((max_frequency, current_frequency))

    return compressed_data


def lossy():
    """
    I mentioned it here only as notice
    DCT (Discrete Cosine Transform)

    """
    pass


@working_time_prec()
def main():
    text = 'Hello world Hello world Hello world Hello world Hello world'
    print(lossless_gigachat(text))


if __name__ == '__main__':
    main()
