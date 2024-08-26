#!/usr/bin/python3
""" code to returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes”.
    """
    grid_width = len(grid[0])
    grid_height = len(grid)
    edges = 0
    land_count = 0

    for x in range(grid_height):
        for y in range(grid_width):
            if grid[x][y] == 1:
                land_count += 1
                if (y > 0 and grid[x][y - 1] == 1):
                    edges += 1
                if (x > 0 and grid[x - 1][y] == 1):
                    edges += 1
    return land_count * 4 - edges * 2
