
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

#Note: You can only move either down or right at any point in time.


class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if i+1 < len(grid) and j+1 < len(grid[0]):
                    grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])
                elif (i+1) < len(grid):
                    grid[i][j] += grid[i+1][j]
                elif (j+1) <len(grid[0]):
                    grid[i][j] +=grid[i][j+1]
        return grid[0][0]