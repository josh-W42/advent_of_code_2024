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


def part_two_solution(ls: list[int]):
    """
    Ok so this time, we can only move a file segment into free space segment.

    General idea

    for all files
        for all free space segments:
            if you can fit a file in to the segment.
                place it
            else:
                skip the file

    still calculate the checksum
    and return it

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

        ids.append([len(disk), index_count, index])
        for j in range(index_count):
            disk.append(index)

        free_spaces.append([len(disk), free_space_count])
        for j in range(free_space_count):
            disk.append('.')

        id_index += 1

    for i in range(len(ids) - 1, -1, -1):
        disk_id_index, id_size, ID = ids[i]

        for j in range(len(free_spaces)):
            disk_free_index, free_size = free_spaces[j]

            # Dont place a file in a free space that occurs after the file.
            if disk_free_index > disk_id_index:
                break

            if id_size <= free_size:

                for k in range(id_size):
                    # set the disk id values to free space
                    disk[disk_id_index + k] = '.'

                    # set the free space to the file
                    disk[disk_free_index + k] = ID

                free_spaces[j] = [disk_free_index + id_size, free_size - id_size]
                break

    # Now calculate the checksum
    result = 0

    for i in range(len(disk)):
        if disk[i] == '.':
            continue

        result += disk[i] * i

    return result


if __name__ == '__main__':
    data = parse_data()
    part_one_solution(data)
    part_two_solution(data)