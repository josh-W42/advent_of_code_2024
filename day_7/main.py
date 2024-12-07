"""
Bridge Repair
"""

import os

input_path = os.path.join(os.curdir, 'input.txt')


def parse_data() -> dict[int, list[int]]:
    result: dict[int, list[int]] = {}

    with open(input_path, 'r') as f:
        for line in f.readlines():
            key, string = line.split(':')
            result[int(key)] = [int(val) for val in string.split(' ') if len(val) > 0]

    return result


def equation_is_possible(target: int, options: list[int], solution: int, index: int):
    if solution > target:
        return False
    if solution == target:
        return True
    if index >= len(options):
        return False

    add_next = equation_is_possible(target, options, solution + options[index], index + 1)
    multiply_next = equation_is_possible(target, options, solution * options[index], index + 1)

    return add_next or multiply_next


def part_one_solution(mp: dict[int, list[int]]):
    """
    We have a dictionary, where for each key
    a list of values must equal the key through a
    series of sum and products of the values.

    - We can't shift the order of the values
    - we can't rearrange the digits of the values.

    We need to take the sum of keys whose values can equal that key.

    I'll use a recursive approach.

    :param mp:
    :return:
    """

    result = 0

    for key in mp.keys():
        value = mp[key]

        if equation_is_possible(key, value, value[0], 1):
            result += key

    return result


if __name__ == '__main__':
    data = parse_data()
    ans = part_one_solution(data)