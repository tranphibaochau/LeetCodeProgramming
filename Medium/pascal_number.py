"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

Could you optimize your algorithm to use only O(k) extra space?

"""

def getRow(rowIndex):
    result = [1] *(rowIndex+1)
    for i in range(2, rowIndex+1):
        for j in range(i-1,0,-1):
            result[j] += result[j-1]
    return result
