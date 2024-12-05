"""
Print Queue
"""

import os

input_file = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[dict[int, set[int]], list[list[int]]]:
    num_map: dict[int, set[int]] = {}
    prints: list[list[int]] = []

    with open(input_file, 'r') as f:
        for line in f:
            if line.find('|') != -1:
                str_key, str_val = line.split('|')
                key, val = int(str_key), int(str_val)

                if key in num_map:
                    num_map[key].add(val)
                else:
                    num_map[key] = {val}
            elif line != '\n':
                prints.append([int(val) for val in line.split(',')])

    return [num_map, prints]


def part_one_solution(rules: dict[int, set[int]], prints: list[list[int]]) -> int:
    """
    So we have a set of rules in a dictionary:

    - Where a key has to appear before any number in the set rules[key].
    - Each number in the set rules[key] might be in rules.

    Then we have a list of prints:

    - We have to determine if the print is in the correct order.
    - A print is in the correct order if each number in the list follows the rules.

    We then take the sum of all the middle values of all the correct prints.
    That sum is the result.

    :param rules:
    :param prints:
    :return:
    """

    result = 0
    for update in prints:
        is_in_correct_order = True

        for i in range(len(update)):
            # Each val in rules[update[i]] cannot be before update[i]

            if update[i] in rules:
                for j in range(i):
                    if update[j] in rules[update[i]]:
                        is_in_correct_order = False
                        break

                if not is_in_correct_order:
                    break

        if is_in_correct_order:
            result += update[len(update) // 2]

    return result


def part_two_solution(rules: dict[int, set[int]], prints: list[list[int]]) -> int:
    """
    See part 1.
    Now we only focus on the incorrect prints.
    We have to create correct print from an incorrect print.

        I purpose that we swap the value that breaks the rules with the value that should
        come before it.
        We repeat this process until it becomes correct.


    Similar to before we take the sum of all the middle values and return the sum.

    :param rules:
    :param prints:
    :return:
    """

    result = 0
    for update in prints:
        is_in_correct_order = True

        for i in range(len(update)):
            # Each val in rules[update[i]] cannot be before update[i]

            if update[i] in rules:
                for j in range(i):
                    if update[j] in rules[update[i]]:
                        is_in_correct_order = False
                        break

                if not is_in_correct_order:
                    break

        if not is_in_correct_order:

            while not is_in_correct_order:
                is_in_correct_order = True
                for i in range(len(update)):
                    if update[i] in rules:
                        for j in range(i):
                            if update[j] in rules[update[i]]:
                                is_in_correct_order = False

                                temp = update[j]
                                update[j] = update[i]
                                update[i] = temp
                                break

            result += update[len(update) // 2]

    return result


def analyze_data(m: dict[int, set[int]], ls: list[list[int]]):
    print('map size: ', len(m))
    min_val_size = float('inf')
    max_val_size = 0
    val_size_sum = 0

    for k in m:
        min_val_size = min(len(m[k]), min_val_size)
        max_val_size = max(len(m[k]), max_val_size)
        val_size_sum += len(m[k])

    print('map min: ', min_val_size)
    print('map max: ', max_val_size)
    print('map average: ', val_size_sum // len(m))
    print('prints size: ', len(ls))

    min_print_size = float('inf')
    max_print_size = 0
    print_size_sum = 0

    for p in ls:
        min_print_size = min(min_print_size, len(p))
        max_print_size = max(max_print_size, len(p))
        print_size_sum += len(p)

    print('list min: ', min_print_size)
    print('list max: ', max_print_size)
    print('list average: ', print_size_sum // len(ls))


if __name__ == '__main__':
    rule_map, prints = parse_data()
    # analyze_data(rule_map, prints)
    ans_1 = part_one_solution(rule_map, prints)
    ans_2 = part_two_solution(rule_map, prints)