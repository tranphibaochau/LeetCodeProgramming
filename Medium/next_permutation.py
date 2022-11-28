"""
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order
then the next permutation of that array is the permutation that follows it in the sorted container.

If such arrangement is not possible, the array must be rearranged as the lowest possible order
(i.e., sorted in ascending order).
"""

def next_permutation(nums):
    """
    The idea is to go from right to left and find the first non-increasing number to be the pivot,
    then passing through from right to left one more time to find the smallest number that is bigger than the pivot,
    we swap these two numbers then revert the substring after the pivot.
    The result will be the next permutation
    """
    # note: in case the string is monotonically decreasing, we simply reverse the whole string
    # this is why we initiate index to be -1
    index = -1

    # start from the end of the list and find the position of the first non-increasing number
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            # doing another pass from right to left to find the first number larger than nums[i]
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            # swap the two numbers
            nums[i], nums[j] = nums[j], nums[i]
            index = i
            break
    # reverse the substring to ensure that it is smallest lexicographically
    nums[index + 1:] = nums[index + 1:][::-1]
