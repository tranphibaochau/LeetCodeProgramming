#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?



def uniquePaths(self, m, n):
    if m == 1 or n == 1:
        return 1
    grid =[[0] * n for _ in range(m)]
    grid[m-1][n-1] = 1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i+1 < m:
                grid[i][j] += grid[i+1][j]
            if j+1 < n:
                grid[i][j] += grid[i][j+1]
    return grid[0][0]