"""
Garden Groups
"""

import os
from functools import cmp_to_key

input_path = os.path.join(os.curdir, 'input.txt')


def parse_data() -> list[list[str]]:
    result = []

    with open(input_path, 'r') as f:
        for line in f:
            result.append([val for val in line if val != '\n'])

    return result


def part_one_solution(mat: list[list[str]]) -> int:
    """
    We have matrix, they all have strings.
    Strings that are similar and are adjacent form a region.

    We need to calculate the perimeter and the area of each region.
    Multiply those values together.
    Take the sum of those values.
    Then return the sum.

    :param mat:
    :return:
    """

    result = 0

    # so we do not recalculate regions we've already traveled
    visited_regions = set()

    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if (i, j) in visited_regions:
                continue

            stack = [(i, j)]
            origin = mat[i][j]
            visited_regions.add((i, j))

            # So points that we've visited do not re-enter the stack.
            # but we still recognize other regions as foreign, even if we've
            # already traversed them.
            inner_visited = {(i, j)}

            # Calculate the perimeter by counting all sides that are not adjacent to the origin letter.
            perimeter = 0

            # The area in this case can be counted by counting all
            # the blocks that have the origin letter
            area = 0

            while stack:
                node = stack.pop()
                a, b = node

                area += 1

                if a == 0 or a == len(mat) - 1:
                    perimeter += 1

                if b == 0 or b == len(mat[0]) - 1:
                    perimeter += 1

                if a - 1 >= 0 and (a - 1, b) not in inner_visited:

                    if mat[a - 1][b] == origin:
                        visited_regions.add((a - 1, b))
                        stack.append((a - 1, b))
                        inner_visited.add((a - 1, b))
                    else:
                        perimeter += 1

                if a + 1 < len(mat) and (a + 1, b) not in inner_visited:

                    if mat[a + 1][b] == origin:
                        visited_regions.add((a + 1, b))
                        stack.append((a + 1, b))
                        inner_visited.add((a + 1, b))
                    else:
                        perimeter += 1

                if b - 1 >= 0 and (a, b - 1) not in inner_visited:

                    if mat[a][b - 1] == origin:
                        visited_regions.add((a, b - 1))
                        stack.append((a, b - 1))
                        inner_visited.add((a, b - 1))
                    else:
                        perimeter += 1

                if b + 1 < len(mat[0]) and (a, b + 1) not in inner_visited:

                    if mat[a][b + 1] == origin:
                        visited_regions.add((a, b + 1))
                        stack.append((a, b + 1))
                        inner_visited.add((a, b + 1))
                    else:
                        perimeter += 1

            result += perimeter * area

    return result


def compare_x(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]

    return a[1] - b[1]


def compare_y(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]

    return a[0] - b[0]


def part_two_solution(mat: list[list[str]]) -> int:
    """
    Similar to before, only now we calculate the perimeter by finding the
    number of sides for the region.

    So we take the points on the edges and sort them by they're respective directions in ascending order
    and look at them in pairs. if they're right next to each other, they only are counted as a single segment otherwise
    they're counted as two segments.

    :param mat:
    :return:
    """

    result = 0

    # so we do not recalculate regions we've already traveled
    visited_regions = set()

    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if (i, j) in visited_regions:
                continue

            stack = [(i, j)]
            origin = mat[i][j]
            visited_regions.add((i, j))

            # So points that we've visited do not re-enter the stack.
            # but we still recognize other regions as foreign, even if we've
            # already traversed them.
            inner_visited = {(i, j)}

            # The area in this case can be counted by counting all
            # the blocks that have the origin letter
            area = 0

            sides = {'+y': [], '-y': [], '+x': [], '-x': []}
            while stack:
                node = stack.pop()
                a, b = node
                area += 1

                if a == 0 or a == len(mat) - 1:
                    if a == 0:
                        sides['-y'].append((-1, b))

                    else:
                        sides['+y'].append((len(mat), b))

                if b == 0 or b == len(mat[0]) - 1:
                    if b == 0:
                        sides['-x'].append((a, -1))

                    else:
                        sides['+x'].append((a, len(mat[0])))

                if a - 1 >= 0 and (a - 1, b) not in inner_visited:

                    if mat[a - 1][b] == origin:
                        visited_regions.add((a - 1, b))
                        stack.append((a - 1, b))
                        inner_visited.add((a - 1, b))
                    else:
                        sides['-y'].append((a - 1, b))

                if a + 1 < len(mat) and (a + 1, b) not in inner_visited:

                    if mat[a + 1][b] == origin:
                        visited_regions.add((a + 1, b))
                        stack.append((a + 1, b))
                        inner_visited.add((a + 1, b))
                    else:
                        sides['+y'].append((a + 1, b))

                if b - 1 >= 0 and (a, b - 1) not in inner_visited:

                    if mat[a][b - 1] == origin:
                        visited_regions.add((a, b - 1))
                        stack.append((a, b - 1))
                        inner_visited.add((a, b - 1))
                    else:
                        sides['-x'].append((a, b - 1))

                if b + 1 < len(mat[0]) and (a, b + 1) not in inner_visited:

                    if mat[a][b + 1] == origin:
                        visited_regions.add((a, b + 1))
                        stack.append((a, b + 1))
                        inner_visited.add((a, b + 1))
                    else:
                        sides['+x'].append((a, b + 1))

            # Begin segment side counting.
            sides['+x'].sort(key=cmp_to_key(compare_x))
            right_side = 0 if len(sides['+x']) == 0 else 1

            for j in range(len(sides['+x']) - 1):
                y_1, x_1 = sides['+x'][j]
                y_2, x_2 = sides['+x'][j + 1]

                if x_1 == x_2 and y_1 + 1 != y_2:
                    right_side += 1
                elif x_1 != x_2:
                    right_side += 1

            sides['-x'].sort(key=cmp_to_key(compare_x))
            left_side = 0 if len(sides['-x']) == 0 else 1

            for j in range(len(sides['-x']) - 1):
                y_1, x_1 = sides['-x'][j]
                y_2, x_2 = sides['-x'][j + 1]

                if x_1 == x_2 and y_1 + 1 != y_2:
                    left_side += 1
                elif x_1 != x_2:
                    left_side += 1

            sides['+y'].sort(key=cmp_to_key(compare_y))
            up_side = 0 if len(sides['+y']) == 0 else 1

            for j in range(len(sides['+y']) - 1):
                y_1, x_1 = sides['+y'][j]
                y_2, x_2 = sides['+y'][j + 1]

                if y_1 == y_2 and x_1 + 1 != x_2:
                    up_side += 1
                elif y_1 != y_2:
                    up_side += 1

            sides['-y'].sort(key=cmp_to_key(compare_y))
            down_side = 0 if len(sides['-y']) == 0 else 1

            for j in range(len(sides['-y']) - 1):
                y_1, x_1 = sides['-y'][j]
                y_2, x_2 = sides['-y'][j + 1]

                if y_1 == y_2 and x_1 + 1 != x_2:
                    down_side += 1
                elif y_1 != y_2:
                    down_side += 1

            side_count = right_side + left_side + up_side + down_side
            result += side_count * area

    return result


if __name__ == '__main__':
    data = parse_data()
    ans_1 = part_one_solution(data)
    ans_2 = part_two_solution(data)