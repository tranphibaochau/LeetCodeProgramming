
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. 
#The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#Now consider if some obstacles are added to the grids. How many unique paths would there be?

def uniquePathsWithObstacles(self, obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    if obstacleGrid[m-1][n-1] == 1: #if destination is blocked, return 0
        return 0
    #build answer grid
    grid =[[0] * n for _ in range(m)]
    grid[m-1][n-1] = 1 #destination (if not blocked) is 1
    #bottom-up DP
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
        	#if there is an obstacle, the path on and through that spot is no longer valid
            if obstacleGrid[i][j] == 1:
                grid[i][j] = 0
            else:
                if i+1 < m:
                    grid[i][j] += grid[i+1][j]
                if j+1 < n:
                    grid[i][j] += grid[i][j+1]
    return grid[0][0]