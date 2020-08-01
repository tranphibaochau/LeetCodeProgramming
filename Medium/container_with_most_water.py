"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Link: https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/2963/
"""


def maxArea(self, height):
    left = 0
    right = len(height)-1
    max_area = min(height[left],height[right])*(right-left)
    while left < right:
        if height[left] < height[right]: #left side is shorter
            shorter = height[left]
            while height[left] <= shorter and left < right: # find the left most verticle line that is larger than the current left side of the container
                left +=1
            max_area = max(max_area, min(height[left],height[right])*(right-left)) #make sure the max_area is larger
        else: # find the right most verticle line that is larger than the current right side of the container
            shorter = height[right]
            while height[right] <= shorter and left < right:
                right -=1
            max_area = max(max_area, min(height[left],height[right])*(right-left))
    return max_area


#Optimal solution found on leetcode:
def maxArea(height):
    left = 0
    right = len(height)-1
    max_area = min(height[left],height[right])*(right-left)
    while left < right:
        max_area = max(max_area, min(height[left],height[right])*(right-left))
        if height[left] > height[right]:
            right-=1
        else:
            left+=1
    return max_area


print(divmod(5, 9))