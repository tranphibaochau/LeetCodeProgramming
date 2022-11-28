import math
from collections import Counter


def three_sum_multiplicity(nums, target):
    nums = sorted(nums)
    print(nums)
    count = Counter(nums)
    total = 0
    def two_sum_multiplicity(nums, n,  target):

        total_2sum = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < (target-n):
                print('left', nums, nums[left], nums[right])
                left += 1
            elif nums[left] + nums[right] > (target-n):
                print("right")
                right -= 1
            else:
                if nums[left] == nums[right] and nums[left] == n:
                    total_2sum += math.factorial(count[n])/(math.factorial(count[n]-3)*math.factorial(3))
                    break
                elif nums[left] == n and nums[left] != nums[right]:
                    total_2sum += count[nums[right]]*count[n]*(count[n]-1)//2
                elif nums[left] == nums[right] and nums[left] != n:
                    total_2sum += count[n] * (count[nums[left]] * (count[nums[left] - 1]) // 2)
                else:
                    total_2sum += count[n] * count[nums[left]] * count[nums[right]]
                left += count[nums[left]]
                right -= count[nums[right]]
                print(total_2sum, n, nums[left], nums[right])
        return total_2sum

    i = 0
    while i < len(nums) and nums[i] <= target//3:
        new_target = target - nums[i]
        temp_total = two_sum_multiplicity(nums[i+1:], nums[i], target)
        total += temp_total
        i += count[nums[i]]

    return total


test1 = [1,1,2,2,3,3,4,4,5,5]
print(three_sum_multiplicity(test1, 8))
