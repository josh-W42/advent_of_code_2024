"""
Hoof It
"""

import os

input_file = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[list[int]]:
    result = []

    with open(input_file, 'r') as f:
        for line in f:
            result.append([int(val) for val in line if val != '\n'])

    return result


def part_one_solution(mat: list[list[int]]):
    """
    So we have matrix of integers representing a topographic map.
    Each number represents a height from [0, 9].

    A trail always starts at 0 and ends at 9.
    A trail is scored by the number of times you can travel from the start to a end.
    You can only travel upwards one step at a time.

    So if we treat this like a graph.
    Find all the starts.
    for each start
        Use something like BFS.
        Count the number of 9s we reach

    return the total number

    :param mat:
    :return:
    """

    ends_reached = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                continue

            stack = [[(i, j), 1]]
            ends = 0
            summits = set()

            while stack:
                node, next_val = stack.pop()
                a, b = node

                if a - 1 >= 0 and mat[a - 1][b] == next_val:
                    if next_val == 9:
                        if (a - 1, b) not in summits:
                            summits.add((a - 1, b))
                            ends += 1
                    else:
                        stack.append([(a - 1, b), next_val + 1])

                if a + 1 < len(mat) and mat[a + 1][b] == next_val:

                    if next_val == 9:
                        if (a + 1, b) not in summits:
                            summits.add((a + 1, b))
                            ends += 1
                    else:
                        stack.append([(a + 1, b), next_val + 1])

                if b - 1 >= 0 and mat[a][b - 1] == next_val:

                    if next_val == 9:
                        if (a, b - 1) not in summits:
                            summits.add((a, b - 1))
                            ends += 1
                    else:
                        stack.append([(a, b - 1), next_val + 1])

                if b + 1 < len(mat[0]) and mat[a][b + 1] == next_val:

                    if next_val == 9:
                        if (a, b + 1) not in summits:
                            summits.add((a, b + 1))
                            ends += 1
                    else:
                        stack.append([(a, b + 1), next_val + 1])

            ends_reached += ends

    return ends_reached


if __name__ == '__main__':
    data = parse_data()
    print(part_one_solution(data))