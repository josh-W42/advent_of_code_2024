"""
Plutonian Pebbles
"""

import os

input_file = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[int]:
    with open(input_file, 'r') as f:
        result = [int(val) for val in f.readlines()[0].split(' ')]

    return result


def part_one_solution(ls: list[int]) -> int:
    """
    So you have a list of integers and a set of rules.

    after every cycle (blinking) a number (stone) will do something:
        if the number is == 0:
            the number becomes 1
        if the number is even:
            the number is split into two where the left side of the digits are
            now on left stone and the right side of the digits are now on the
            right stone.

            With leading zeros removed
        else:
            the number is multiplied by 2024

    At the end of 25 cycles
    you have to count the number of stones you have left
    and return that number

    :param ls:
    :return:
    """

    current_stones = []
    next_stones = ls

    for _ in range(25):

        current_stones = next_stones.copy()
        next_stones = []

        for i in range(len(current_stones)):
            stone = current_stones[i]
            str_stone = str(stone)

            if stone == 0:
                next_stones.append(1)
            elif len(str_stone) % 2 == 0:
                ls_stone = [val for val in str_stone]

                left = ls_stone[:len(ls_stone) // 2]
                right = ls_stone[len(ls_stone) // 2:]

                for j in range(len(right)):
                    if right[j] != '0':
                        right = right[j:]
                        break

                next_stones.append(int("".join(left) or 0))
                next_stones.append(int("".join(right) or 0))
            else:
                next_stones.append(stone * 2024)

    return len(next_stones)


if __name__ == '__main__':
    data = parse_data()
    print(part_one_solution(data))