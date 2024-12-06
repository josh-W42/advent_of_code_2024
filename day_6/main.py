"""
Guard Gallivant
"""

import os

input_path = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[list[str]]:
    result: list[list[str]] = []

    with open(input_path, 'r') as f:
        for line in f:
            result.append([s for s in line if s != '\n'])

    return result


def part_one_solution(matrix: list[list[str]]) -> int:
    """
    In a n x n matrix, there are obstacles '#' and a single guard '^' facing north.
    in one turn the guard will advance in the direction they're facing.
    when an obstacle is immediately in front of the guard it will turn 90 degrees to the right.

    Eventually the guard will exit the grid. (reach edge of the matrix)

    Find all the distinct locations the guard has been.
    return that integer.

    :param matrix:
    :return:
    """

    has_been = set()
    current_position = (0, 0)
    objects = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '^':
                current_position = (i, j)
                has_been.add(current_position)
            elif matrix[i][j] == '#':
                objects.add((i, j))

    direction = (-1, 0)
    y, x = current_position
    while 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
        has_been.add((y, x))
        if direction == (-1, 0):
            if (y - 1, x) not in objects:
                y, x = y - 1, x
            else:
                direction = (0, 1)

        elif direction == (0, 1):
            if (y, x + 1) not in objects:
                y, x = y, x + 1
            else:
                direction = (1, 0)

        elif direction == (1, 0):
            if (y + 1, x) not in objects:
                y, x = y + 1, x
            else:
                direction = (0, -1)

        elif direction == (0, -1):
            if (y, x - 1) not in objects:
                y, x = y, x - 1
            else:
                direction = (-1, 0)

    return len(has_been)


if __name__ == '__main__':
    data = parse_data()
    ans = part_one_solution(data)