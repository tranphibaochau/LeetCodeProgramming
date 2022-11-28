#https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

def maximumScore(nums, multipliers):
    dp = [0] * len(multipliers)
    left = 0
    right = len(nums) - 1
    for i in range(0, len(multipliers)):
        if nums[left] * multipliers[i] > nums[right] * multipliers[i]:
            if i > 0:
                dp[i] = dp[i - 1] + nums[left] * multipliers[i]
            else:
                dp[i] = nums[left] * multipliers[i]
            left += 1
        else:
            if i > 0:
                dp[i] = dp[i - 1] + nums[right] * multipliers[i]
            else:
                dp[i] = nums[right] * multipliers[i]
            right -= 1
    print(dp)
    return dp[len(multipliers)-1]

nums1, multiplier1 = [1, 2, 3], [3, 2, 1]
nums2, multiplier2 = [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]
print(maximumScore(nums2, multiplier2))