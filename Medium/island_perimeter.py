"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). 

The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 

One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.


Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

"""

#the intuition is that if a cell is part of an island, add the total of number to 4, 
#then if it is neighbored with another UP or LEFT cell that is 1, subtract by 2 for each neighbor
def islandPerimeter(grid):
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4
                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2
                        
                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2
        return result