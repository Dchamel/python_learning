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


def data_preparation(path_to_input_file: str) -> tuple[list, list]:
    """Takes line from a file trough Generator function and returns two sorted lists"""

    left_list, right_list = [], []
    for line in read_data_line(path_to_input_file):
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    return left_list, right_list


def calculate_distance(sorted_datalists: tuple) -> int:
    """Calculates the distance between elements in two lists and summarize it"""

    left_list, right_list = sorted_datalists
    distance = 0
    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])

    return distance


def calculate_similarity(sorted_datalists: tuple[list, list]) -> int:
    """
    Calculates similarity between left and right lists
    Element from left list multiplies on count of it from right list and sums result of this operation
    """

    left_list, right_list = sorted_datalists
    similarity = 0
    for element in left_list:
        similarity += right_list.count(element) * element

    return similarity


@working_time_prec(8)
def main() -> None:
    """Func for run other funcs"""

    print(calculate_distance(data_preparation(INPUT_FILE)))
    print(calculate_similarity(data_preparation(INPUT_FILE)))
    pass


if __name__ == '__main__':
    main()
