"""
Resonant Collinearity
"""

import os

inout_path = os.path.join(os.curdir, "input.txt")


def parse_data() -> list[list[str]]:
    result = []

    with open(inout_path, 'r') as f:
        for line in f:
            result.append([val for val in line if val != '\n'])

    return result


def part_one_solution(mat: list[list[str]]) -> int:
    """
    A matrix, full of nodes. Each node must pair with another node of each type.
    The pairing of two nodes creates a pair of anti-nodes that is twice the distance
    away from the original nodes.

    The goal is to count all the unique locations of anti-nodes in the matrix.

    By knowing which pair comes first in the x perspective
    and which pair comes first in the y perspective we can find
    the anti-pairs by adding or subtracting the absolute differences
    between the x and y values of the pairs

    :param mat:
    :return:
    """

    nodes = {}

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '.':
                continue

            if mat[i][j] in nodes:
                nodes[mat[i][j]].append((i, j))
            else:
                nodes[mat[i][j]] = [(i, j)]

    anti_nodes = set()

    for node in nodes:
        for i in range(len(nodes[node])):
            first = nodes[node][i]
            for j in range(i + 1, len(nodes[node])):
                second = nodes[node][j]
                delta_y = abs(first[0] - second[0])
                delta_x = abs(first[1] - second[1])

                # Determine which is truly first from left to right
                # Then determine which is truly first from top to bottom

                anti_node_left_x = 0
                anti_node_left_y = 0

                anti_node_right_x = 0
                anti_node_right_y = 0

                if first[1] < second[1]:
                    anti_node_left_x = first[1] - delta_x
                    anti_node_right_x = second[1] + delta_x

                    if first[0] < second[0]:
                        anti_node_left_y = first[0] - delta_y
                        anti_node_right_y = second[0] + delta_y
                    else:
                        anti_node_left_y = first[0] + delta_y
                        anti_node_right_y = second[0] - delta_y

                else:
                    anti_node_left_x = second[1] - delta_x
                    anti_node_right_x = first[1] + delta_x

                    if second[0] < first[0]:
                        anti_node_left_y = second[0] - delta_y
                        anti_node_right_y = first[0] + delta_y
                    else:
                        anti_node_left_y = second[0] + delta_y
                        anti_node_right_y = first[0] - delta_y

                if (0 <= anti_node_left_y < len(mat)) and (0 <= anti_node_left_x < len(mat[0])):
                    anti_nodes.add((anti_node_left_y, anti_node_left_x))

                if (0 <= anti_node_right_y < len(mat)) and (0 <= anti_node_right_x < len(mat[0])):
                    anti_nodes.add((anti_node_right_y, anti_node_right_x))

    return len(anti_nodes)


if __name__ == '__main__':
    data = parse_data()
    ans = part_one_solution(data)