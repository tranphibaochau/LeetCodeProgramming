#Given a 2D binary matrix filled with 0's and 1's (in string form), find the largest square containing only 1's and return its area.


def maximalSquare(self, matrix):
    max_value = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if int(matrix[i][j]) == 1 and i>=1 and j>=1:
                matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1
            max_value = max(max_value, int(matrix[i][j]))
    return max_value*max_value