def binary_search_larger(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left+right)//2
        if mid > 0 and (nums[mid] >= target) and (nums[mid-1] < target):
            return nums[mid]
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid
    return nums[right]

nums = [1, 3, 5, 6, 9, 12, 15, 20, 21, 23, 30]
print(binary_search_larger(nums, 1))
print(binary_search_larger(nums, 18))
print(binary_search_larger(nums, 10))
print(binary_search_larger(nums, 4))