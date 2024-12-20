"""
Historian Hysteria
"""
import os

current_dir = os.path.join(os.getcwd(), 'day_1')
data_path = os.path.join(current_dir, 'input.txt')

"""
Data is n = 1000
"""


"""
Goal:
Find the sum of the differences between two columns of data in sorted order.
Initially the data is unsorted.
An O(n log n) solution could be made.
"""
def part_one_solution(l1: list[int], l2: list[int]) -> int:
    l1.sort()
    l2.sort()

    result = 0

    for i in range(len(l1)):
        result += abs(l1[i] - l2[i])

    return result


"""
Goal:
Find a total similarity score.
O(n) time O(n) space solution
Use a dictionary, count the frequency of each value of l2.
Loop through l1:
    if in dictionary:
        add similarity score to result
"""
def part_two_solution(l1: list[int], l2: list[int]) -> int:
    result = 0

    freq = {}
    for val in l2:
        if val in freq:
            freq[val] += 1
        else:
            freq[val] = 1

    for val in l1:
        if val in freq:
            result += freq[val] * val

    return result


def parse_data() -> [list[int], list[int]]:
    col_1 = []
    col_2 = []
    with open(data_path, 'r') as f:
        for line in f:
            result = line.split(' ')
            col_1.append(int(result[0]))
            col_2.append(int(result[-1]))

    return [col_1, col_2]


if __name__ == '__main__':
    [a, b] = parse_data()
    part_one = part_one_solution(a, b)
    part_two = part_two_solution(a, b)
