from MyProjects.MyModules.time_additional import working_time_prec

INPUT_FILE = 'input/input.txt'


def read_data_line(path_to_input_file: str) -> str:
    """read line from a file"""

    try:
        with open(path_to_input_file, 'r') as file:
            for line in file:
                yield line.strip()
    except Exception as err:
        print(f'File open error: {err}')


def data_preparation(path_to_input_file: str):
    """Takes line from a file trough Generator function and returns two sorted lists"""

    all_lines = []
    for line in read_data_line(path_to_input_file):
        all_lines.append([i for i in line.split()])

    return all_lines


def data_processing(data: list[list[str]]):
    """Calculates quantity of good reports"""

    good = 0
    for line in data:
        for i in range(len(line)):
            if i == len(line) - 1:
                good += 1
                break
            elif abs(int(line[i]) - int(line[i + 1])) == 0:
                break
            elif abs(int(line[i]) - int(line[i + 1])) <= 2:
                continue
            else:
                break

    print(good)


@working_time_prec(8)
def main() -> None:
    """Func for run other funcs"""

    data_processing(data_preparation(INPUT_FILE))

    pass


if __name__ == '__main__':
    main()
