"""
 Red-Nosed Reports
"""

import os

input_file = os.path.join(os.getcwd(), 'input.txt')

"""
Data is n = 1000
"""


def parse_data() -> list[list[int]]:
    results = []
    with open(input_file, 'r') as f:
        for line in f:
            results.append([int(num) for num in line.split(' ')])
    return results


def part_one_solution(data: list[list[int]]) -> int:
    """
    Count the number of 'safe' rows in the data.

    A row is 'safe' if:
        - It is strictly increasing or decreasing
        - The difference between any two adjacent levels is in the range [1, 3].

    :param data: input data
    :return: The number of safe rows.
    """

    result = 0
    for row in data:

        is_safe = True

        is_increasing = row[0] < row[1]

        for i in range(len(row) - 1):
            if row[i] > row[i + 1] and is_increasing:
                is_safe = False
                break

            if row[i] < row[i + 1] and not is_increasing:
                is_safe = False
                break

            diff = abs(row[i] - row[i + 1])
            if diff < 1 or diff > 3:
                is_safe = False
                break

        if is_safe:
            result += 1

    return result


if __name__ == '__main__':
    results = parse_data()
    part_one = part_one_solution(results)

    print(part_one)
