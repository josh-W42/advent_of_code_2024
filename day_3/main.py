"""
Mull it over
"""

import os
import re


input_path = os.path.join(os.curdir, 'input.txt')
pattern = re.compile(r'mul\(\d*,\d*\)')

updated_pattern = re.compile(r'don\'t\(\)|do\(\)|mul\(\d*,\d*\)')
START_SEQUENCE = 'do()'
STOP_SEQUENCE = 'don\'t()'


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


def part_two_solution(ls: list[str]) -> int:
    """
    Similar to one BUT, now there are START and STOP commands.
    START and STOP patterns are all the same.
    Initially we're in a START state.

    ANY regular patterns found after a STOP command and before a START command do not count.

    :param ls:
    :return:
    """

    result = 0
    should_process = True
    for line in ls:
        for match in updated_pattern.findall(line):
            if match == START_SEQUENCE:
                should_process = True
            elif match == STOP_SEQUENCE:
                should_process = False
            elif should_process:
                substring: list[str] = match[4:len(match) - 1].split(',')
                p1, p2 = substring

                result += int(p1) * int(p2)

    return result


if __name__ == '__main__':
    data = parse_data()
    ans = part_one_solution(data)
    ans2 = part_two_solution(data)




