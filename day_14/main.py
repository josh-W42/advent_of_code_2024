"""
Restroom Redoubt
"""

import os
from typing import Tuple

input_path = os.path.join(os.curdir, "input.txt")


# Test input is n = 7, m = 11


def parse_data() -> list[list[Tuple[int, int], Tuple[int, int]]]:
    result = []
    with open(input_path, 'r') as f:
        for line in f:
            point, velocity = line.split(' ')
            point = point[2:].split(',')
            point = (int(point[0]), int(point[1]))
            velocity = velocity[2:].split(',')

            if velocity[0][0] == '-':
                velocity[0] = int(velocity[0][1:]) * -1
            else:
                velocity[0] = int(velocity[0])

            if velocity[1][0] == '-':
                velocity[1] = int(velocity[1][1:]) * -1
            else:
                velocity[1] = int(velocity[1])

            velocity = (velocity[0], velocity[1])

            result.append([point, velocity])

    return result


def part_one_solution(ls: list[list[Tuple[int, int], Tuple[int, int]]], n: int, m: int):
    """
    We have a list that contains tuple pairs, one pair for a position of a robot, another it's velocity.
    after 100 turns we have to find the updated positions of the robots.
    
    we can store this in matrix.
    
    Then we segment this matrix into 4 quadrants, ignoring the horizontal and vertical centers.

    Count the robots in each segment and then return the product of all the counts.

    :param ls: 
    :param n:
    :param m:
    :return: 
    """

    mat = [[0 for _ in range(m)] for _ in range(n)]

    for [start, _] in ls:
        x, y = start
        mat[y][x] += 1

    for _ in range(100):
        for i in range(len(ls)):
            [position, velocity] = ls[i]
            delta_x, delta_y = velocity

            new_position = [0, 0]

            if position[0] + delta_x < 0:
                remainder = 0 - (position[0] + delta_x)
                new_position[0] = m - remainder

            elif position[0] + delta_x >= m:
                remainder = position[0] + delta_x - m
                new_position[0] = 0 + remainder
            else:
                new_position[0] = position[0] + delta_x

            if position[1] + delta_y < 0:
                remainder = 0 - (position[1] + delta_y)
                new_position[1] = n - remainder

            elif position[1] + delta_y >= n:
                remainder = position[1] + delta_y - n
                new_position[1] = 0 + remainder
            else:
                new_position[1] = position[1] + delta_y

            mat[position[1]][position[0]] -= 1
            mat[new_position[1]][new_position[0]] += 1

            ls[i][0] = (new_position[0], new_position[1])

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for i in range(n):
        for j in range(m):
            if i < n // 2 and j < m // 2:
                q1 += mat[i][j]
            elif i > n // 2 and j < m // 2:
                q2 += mat[i][j]
            elif i < n // 2 and j > m // 2:
                q3 += mat[i][j]
            elif i > n // 2 and j > m // 2:
                q4 += mat[i][j]

    return q1 * q2 * q3 * q4


if __name__ == '__main__':
    data = parse_data()
    print(part_one_solution(data, 103, 101))