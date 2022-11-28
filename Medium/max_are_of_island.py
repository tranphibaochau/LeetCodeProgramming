"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

 Output: 6
"""


def max_area_of_island(grid):
    visited = set()
    def DFS(r, c):
        if not (0 <= r < len(grid) and (0 <= c < len(grid[0])) and (r, c) not in visited and grid[r][c] == 1):
            return 0
        visited.add((r, c))
        return (1 + DFS(r+1, c) + DFS(r-1, c) + DFS(r, c+1) + DFS(r, c-1))
    return max(DFS(r, c) for r in range(len(grid)) for c in range(len(grid[0])))