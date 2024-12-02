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


def is_row_safe(row: list[int], is_increasing):
    for i in range(len(row) - 1):
        if row[i] > row[i + 1] and is_increasing:
            return False

        if row[i] < row[i + 1] and not is_increasing:
            return False

        diff = abs(row[i] - row[i + 1])
        if diff < 1 or diff > 3:
            return False

    return True


def part_two_solution(data: list[list[int]]) -> int:
    """
    Count the number of 'safe' rows in the data.

    A row is 'safe' if:
        - It is strictly increasing or decreasing
        - The difference between any two adjacent levels is in the range [1, 3].

    Similar to before, but now if an unsafe row becomes safe after removing one
    item, then that row should be counted as well.

    I define an unsafe value as a value that causes the row to become unsafe.

    Because input side is small (10^3) this is ok but for larger inputs (>= 10^4), this solution would be naive.

    :param data: input data
    :return: The number of safe rows.
    """
    result = 0
    for row in data:

        # Is the unsafe value in the first or last positions?
        # Also, if there isn't an unsafe value at all we end here.
        if is_row_safe(row[1:], row[1] < row[2]) or is_row_safe(row[:len(row) - 1], row[0] < row[1]):
            result += 1
            continue

        for i in range(1, len(row) - 1):
            left = row[:i]
            right = row[i + 1:]

            # is the unsafe value at position i?
            if is_row_safe(left + right, row[i - 1] < row[i + 1]):
                result += 1
                break

    return result


if __name__ == '__main__':
    results = parse_data()
    part_one = part_one_solution(results)
    part_two = part_two_solution(results)
