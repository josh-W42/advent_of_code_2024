"""
Mull it over
"""

import os
import re


input_path = os.path.join(os.curdir, 'input.txt')
pattern = re.compile(r'mul\(\d*,\d*\)')


def parse_data():
    results = []
    with open(input_path, 'r') as f:
        for line in f:
            results.append(line)

    return results


def part_one_solution(ls: list[str]) -> int:
    """
    Given a list, find all substrings that match a pattern.
    For each pattern, multiply two integers separated by a comma and within a set of parenthesis.
    Add all the products of those numbers.

    :param ls:
    :return:
    """
    result = 0
    for line in ls:
        for match in pattern.findall(line):
            substring: list[str] = match[4:len(match) - 1].split(',')
            p1, p2 = substring

            result += int(p1) * int(p2)

    return result





if __name__ == '__main__':
    data = parse_data()
    ans = part_one_solution(data)



