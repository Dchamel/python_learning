# NOT FOR EVERYBODY CODE REVIEW
# if somebody send you here you were cursed by this man =)
# or you just my friend or student

import unittest, re
from time import perf_counter

t1 = perf_counter()


def read_data(path):
    with open(path, 'r') as rawData:
        return rawData.readlines()


def item_list(given_stacks, stack_string, index):
    index_stack = given_stacks[len(given_stacks) - 1].index(stack_string[index])
    item_list = []
    for item in given_stacks[0:len(given_stacks) - 1]:
        try:
            if item[index_stack] != ' ':
                item_list.append(item[index_stack])
        except:
            continue
    return item_list


def raw_data(data_list):
    given_stacks = data_list[0:data_list.index('\n')]
    task_data = data_list[data_list.index('\n') + 1:]
    task_list = []
    for task_line in task_data:
        z = []
        for each in re.findall(r'\d+', task_line.strip()):
            z.append(int(each))
        task_list.append(z)
    return given_stacks, task_list


def stacks_vars(stack_string, item_list, given_stacks):
    all_vars = []
    for index in stack_string:
        locals()[f'stack{index}'] = item_list(given_stacks, stack_string, (int(index) - 1))
        locals()[f'stack{index}'].reverse()
        all_vars.append(locals()[f'stack{index}'])

    return all_vars


def construct_strings(all_vars):
    new_stack = ''
    new_all_stacks = []
    for each_stack in all_vars:
        for cargo in each_stack:
            new_stack += cargo
        new_all_stacks.append(new_stack)
        new_stack = ''

    return new_all_stacks


def elfs_job(input_cargo, task_list):
    for task_line in task_list:
        for _ in range(task_line[0]):
            input_cargo[task_line[2] - 1] += input_cargo[task_line[1] - 1][-1]
            input_cargo[task_line[1] - 1] = input_cargo[task_line[1] - 1][:-1]
    return input_cargo


def last_create(input_cargo):
    all_creates = ''
    for stack in input_cargo:
        all_creates += stack[-1]
    return all_creates


# tests
class AllTests2022Task2(unittest.TestCase):

    def setUp(self) -> None:
        self.path = path
        self.data = ''

    def test01_read_data(self):
        expected = 's'
        actual = read_data(self.path)[3]
        self.assertEqual(expected, actual)


path = 'inputs/task5.txt'
data = read_data(path)
given_stacks, task_list = raw_data(data)

amount_of_stacks = given_stacks[len(given_stacks) - 1].strip().replace(' ', '')
stack_string = amount_of_stacks
amount_of_stacks = int(amount_of_stacks[len(amount_of_stacks) - 1])
input_cargo = construct_strings(stacks_vars(stack_string, item_list, given_stacks))
input_cargo2 = input_cargo.copy()

print(last_create(elfs_job(input_cargo, task_list)))


def part_two(input_cargo2, task_list):
    ic = input_cargo2
    for tl in task_list:
        print(tl, ic)
        ic[tl[2] - 1] += ic[tl[1] - 1][len(ic[tl[1] - 1]) - tl[0]:len(ic[tl[1] - 1])]
        ic[tl[1] - 1] = ic[tl[1] - 1][:len(ic[tl[1] - 1]) - tl[0]]
    return ic


print(last_create(part_two(input_cargo2, task_list)))

# q = 'PZND'
# n = ''
# n = q[len(q) - 3:len(q)]
# q = q[:len(q) - 3]
# print(n, q)

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
