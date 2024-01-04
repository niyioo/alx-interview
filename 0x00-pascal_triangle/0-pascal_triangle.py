#!/usr/bin/python3
""" Pascal triangle module """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows (n).
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1] + [
            prev_row[j - 1] + prev_row[j] for j in range(1, i)
        ] + [1]
        triangle.append(new_row)

    return triangle
