"""
Ceres Search
"""

import os
from enum import Enum

input_path = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[list[str]]:
    result = []
    with open(input_path, 'r') as f:
        for line in f:
            row = []
            for letter in line:
                if letter.isalnum():
                    row.append(letter)

            result.append(row)

    return result


class Directions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    DIAGONAL_UP_LEFT = 5
    DIAGONAL_UP_RIGHT = 6
    DIAGONAL_DOWN_LEFT = 7
    DIAGONAL_DOWN_RIGHT = 8


def part_one_solution(matrix: list[list[str]]):
    """
    So we have matrix of letters.
    We have to find all instances of the word 'XMAS'.
    It could be read forward, backward, vertically, horizontally, Diagonally.

    :param matrix:
    :return:
    """

    target = 'XMAS'

    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != target[0]:
                continue

            stack = [[(i, j), 1, None]]
            while stack:
                point, index, direction = stack.pop()
                a, b = point

                if a - 1 >= 0 and matrix[a - 1][b] == target[index] and (direction == Directions.UP or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a - 1, b), index + 1, Directions.UP])

                if a + 1 < len(matrix) and matrix[a + 1][b] == target[index] and (
                        direction == Directions.DOWN or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a + 1, b), index + 1, Directions.DOWN])

                if b - 1 >= 0 and matrix[a][b - 1] == target[index] and (direction == Directions.LEFT or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a, b - 1), index + 1, Directions.LEFT])

                if b + 1 < len(matrix[0]) and matrix[a][b + 1] == target[index] and (
                        direction == Directions.RIGHT or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a, b + 1), index + 1, Directions.RIGHT])

                if a - 1 >= 0 and b - 1 >= 0 and matrix[a - 1][b - 1] == target[index] and (
                        direction == Directions.DIAGONAL_UP_LEFT or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a - 1, b - 1), index + 1, Directions.DIAGONAL_UP_LEFT])

                if a + 1 < len(matrix) and b - 1 >= 0 and matrix[a + 1][b - 1] == target[index] and (
                        direction == Directions.DIAGONAL_DOWN_LEFT or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a + 1, b - 1), index + 1, Directions.DIAGONAL_DOWN_LEFT])

                if b + 1 < len(matrix[0]) and a - 1 >= 0 and matrix[a - 1][b + 1] == target[index] and (
                        direction == Directions.DIAGONAL_UP_RIGHT or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a - 1, b + 1), index + 1, Directions.DIAGONAL_UP_RIGHT])

                if b + 1 < len(matrix[0]) and a + 1 < len(matrix) and matrix[a + 1][b + 1] == target[index] and (
                        direction == Directions.DIAGONAL_DOWN_RIGHT or not direction):
                    if index == len(target) - 1:
                        result += 1
                    else:
                        stack.append([(a + 1, b + 1), index + 1, Directions.DIAGONAL_DOWN_RIGHT])

    return result


if __name__ == '__main__':
    data = parse_data()
    ans = part_one_solution(data)