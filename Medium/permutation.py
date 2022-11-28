def permute(nums):
    def backtrack(first):
        if first == len(nums):
            output.append(nums[:])
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first+1)
            nums[first], nums[i] = nums[i], nums[first]
    output = []
    backtrack(0)
    return output
nums = [1, 2, 3]
output = permute(nums)
print(output)
