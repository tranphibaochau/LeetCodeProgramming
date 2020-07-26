
"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


def maxProduct(nums) -> int:
    min_so_far = 0
    max_so_far = 0
    
    for i, n in enumerate(nums):
        if i == 0:
            result, min_so_far, max_so_far = nums[0], nums[0], nums[0]
        else:
            temp_min, temp_max = min_so_far, max_so_far
            
            min_so_far = min(n, temp_min*n, temp_max*n)
            max_so_far = max(n, temp_min*n, temp_max*n)
        result = max(result, max_so_far)
    
    return result