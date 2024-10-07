#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
         returns a list of lists of
         integers representing 
         the Pascal’s triangle
         Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    p_triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(p_triangle[i - 1][j - 1] + p_triangle[i - 1][j])
        row.append(1)
        p_triangle.append(row)
    return p_triangle
