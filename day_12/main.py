"""
Garden Groups
"""

import os

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


if __name__ == '__main__':
    data = parse_data()
    print(part_one_solution(data))