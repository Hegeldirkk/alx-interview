#!/usr/bin/python3
""" Interview ALX
SE: Diabakate Ikary
Challenge: Island Perimeter
"""


def island_perimeter(grid):
    """island perimenter function"""
    resultat = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                resultat += 4
                if i > 0 and grid[i-1][j] == 1:
                    resultat -= 2
                if j > 0 and grid[i][j-1] == 1:
                    resultat -= 2
    return resultat
