"""
Plutonian Pebbles
"""

import os

input_file = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[int]:
    with open(input_file, 'r') as f:
        result = [int(val) for val in f.readlines()[0].split(' ')]

    return result


def solution(ls: list[int], blinks: int) -> int:
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

    part 1 is 25 blinks, part 2 is 75.

    :param ls:
    :return:
    """

    current_stones = []
    next_stones = ls

    stone_map: dict[int, list[int]] = {}

    for c in range(blinks):
        print(c)

        current_stones = next_stones.copy()
        next_stones = []

        for i in range(len(current_stones)):
            stone = current_stones[i]
            str_stone = str(stone)

            if stone in stone_map:
                for s in stone_map[stone]:
                    next_stones.append(s)

                continue

            if stone == 0:
                next_stones.append(1)
            elif len(str_stone) % 2 == 0:
                half = len(str_stone) // 2

                left = str_stone[:half]
                right = str_stone[half:]

                if right[0] == '0':
                    for j in range(len(right)):
                        if right[j] != '0':
                            right = right[j:]
                            break

                result_left = int(left or 0)
                result_right = int(right or 0)

                next_stones.append(result_left)
                next_stones.append(result_right)

                stone_map[stone] = [result_left, result_right]
            else:
                product = stone * 2024
                next_stones.append(product)
                stone_map[stone] = [product]

    return len(next_stones)


if __name__ == '__main__':
    data = parse_data()
    print(solution(data, 25))
    # print(solution(data, 75))