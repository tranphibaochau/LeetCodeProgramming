#Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

#For example, given the following triangle
#
#[
#     [2],
#    [3,4],
#  [6,5,7],
#  [4,1,8,3]
#]

#The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.



class Solution:
    #Top-Down Approach
    def minimumTotal(self, triangle):
        if not triangle:
            return []
        if len(triangle) == 1:
            return triangle[0][0]
        
        min_paths = [triangle[0][0]]
        for i in range(1, len(triangle)):
            new_paths = [min_paths[0]+triangle[i][0]]
            for j in range(1, len(triangle[i])-1):
                new_paths.append(min(min_paths[j-1], min_paths[j])+triangle[i][j])
            new_paths.append(min_paths[-1]+triangle[i][-1])
            min_paths = new_paths
        
        return min(min_paths)

    #Bottom-Up Approach
    def minimumTotalBU(self, triangle):
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]