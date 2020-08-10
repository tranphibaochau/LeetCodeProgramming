"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

"""

"""
Iterate over the array and for every element x in the array, negate the value at index abs(x)-1.
The negation operation effectively marks the value abs(x) as seen / visited.

Iterate over the array again, for every element x in the array:
If the value at index abs(x)-1 is positive, it must have been negated twice. Thus abs(x) must have appeared twice in the array. We add abs(x) to the result.
In the above case, when we reach the second occurrence of abs(x), we need to avoid fulfilling this condition again. So, we'll additionally negate the value at index abs(x)-1.
"""
def findDuplicates(nums):
    res = []
    for x in nums:
        if nums[abs(x)-1] < 0:
            res.append(abs(x))
        else:
            nums[abs(x)-1] *= -1
            print(nums)
    return res