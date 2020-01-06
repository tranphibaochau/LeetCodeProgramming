#############################################################################################################################################################
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
# Input: 
#       nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
#.      The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
#.      Also, 3 is the first index where this occurs.
#############################################################################################################################################################


#Solution: calculate the sum of the whole array, then as we go through each number in the array, calculate the sumL and sumR as we see below
def pivotIndex(self, nums):
        sumL = 0
        sumR = sum(nums)
        for i in range(len(nums)):
            sumR -= nums[i]
            if sumL == sumR:
                return i
            sumL += nums[i]
        return -1