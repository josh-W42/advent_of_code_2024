"""
Disk Fragmenter
"""

import os

input_path = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[int]:
    result = []
    with open(input_path, 'r') as f:
        result = [int(val) for val in f.readlines()[0] if val != '\n']

    return result


def part_one_solution(ls: list[int]):
    """
    We have a list. at every even index we have an ID that takes up ls[i] space
    At every odd index we have free space taking ls[i] space.

    Our goal is to pop ID values from the end of the data into the free spaces starting from the left
    side of the data stream.

    Then calculate and return the checksum.

    :param ls:
    :return: Then
    """

    id_index = 0

    free_spaces = []
    ids = []

    disk = []

    for i in range(0, len(ls), 2):
        index = id_index
        index_count = ls[i]

        free_space_count = 0
        if i + 1 < len(ls):
            free_space_count = ls[i + 1]

        for j in range(index_count):
            ids.append(len(disk))
            disk.append(index)

        for j in range(free_space_count):
            free_spaces.append(len(disk))
            disk.append('.')

        id_index += 1

    # so now use the ids and free_spaces lists as stacks
    free_spaces.reverse()

    while free_spaces:

        last = ids.pop()
        if '.' in disk[:last]:
            disk[free_spaces.pop()] = disk[last]
            disk[last] = '.'
        else:
            break

    # Now calculate the checksum
    result = 0

    for i in range(len(disk)):
        if disk[i] == '.':
            break

        result += disk[i] * i

    return result


if __name__ == '__main__':
    data = parse_data()
    part_one_solution(data)