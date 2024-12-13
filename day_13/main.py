"""
Claw Contraption
"""

import os
from typing import Tuple

input_path = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[list[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]:
    values = None
    with open(input_path, 'r') as f:
        values = f.readlines()

    result = []
    for i in range(0, len(values), 4):
        button_1 = values[i].split(':')[1][1:-1].split(' ')
        button_1[0] = int(button_1[0][2:-1])
        button_1[1] = int(button_1[1][2:])

        button_2 = values[i + 1].split(':')[1][1:-1].split(' ')
        button_2[0] = int(button_2[0][2:-1])
        button_2[1] = int(button_2[1][2:])

        prize = [val.split('=')[1] for val in values[i + 2].split(':')[1][1:-1].split(' ')]
        prize[0] = int(prize[0][:-1])
        prize[1] = int(prize[1])

        result.append([tuple(button_1), tuple(button_2), tuple(prize)])

    return result


def dp(point: Tuple[int, int], target: Tuple[int, int], tokens: int, choice_a: Tuple[int, int],
       choice_b: Tuple[int, int], mem: dict[Tuple[int, int], int]):
    if point[0] > target[0]:
        return float('inf')

    if point[1] > target[1]:
        return float('inf')

    if point == target:
        return tokens

    if point not in mem:
        new_point_a = (point[0] + choice_a[0], point[1] + choice_a[1])
        tokens_if_a = dp(new_point_a, target, tokens + 3, choice_a, choice_b, mem)

        new_point_b = (point[0] + choice_b[0], point[1] + choice_b[1])
        tokens_if_b = dp(new_point_b, target, tokens + 1, choice_a, choice_b, mem)

        mem[point] = min(tokens_if_a, tokens_if_b)

    return mem[point]


def part_one_solution(ls: list[list[Tuple[int, int], Tuple[int, int], Tuple[int, int]]]):
    """
    We have a list of triplets,
    within each triplet are pairs of numbers

    the first pair yields the x, y translation if button A was pressed
    the second pair is the same but if Button B was pressed.
    the third pair represents the target point.

    We want to press either a or b buttons in order to reach the target.

    Pressing button A costs 3 tokens.
    Pressing button B costs 1 token.

    We want to spend the minimum amount of tokens to reach the target.

    We also want ot reach all the targets for every triplet.

    The goal then is to take the sum of all the minimum tokens
    needed to reach all achievable targets.

    We can do this with a recursive dynamic programming solution.

    :param ls:
    :return:
    """

    result = 0
    for i in range(len(ls)):
        [button_a, button_b, prize] = ls[i]
        min_tokens = dp((0, 0), prize, 0, button_a, button_b, {})

        if min_tokens != float('inf'):
            result += min_tokens

    return result


if __name__ == '__main__':
    data = parse_data()
    print(part_one_solution(data))