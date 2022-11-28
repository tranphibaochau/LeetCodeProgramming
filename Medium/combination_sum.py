def combination_sum(candidates, target):
    result = []

    def backtrack(index, stack, current_sum=0):
        # if current sum equals to the target, add the current combination to the result
        if current_sum == target:
            result.append(list(stack))
            return

        # if current sum exceeds the target, terminate the current loop
        elif current_sum > target:
            return

        # keep adding the same candidate until the current sum is equal to or greater than the target
        # before popping and move to the next candidate and do the same
        for i in range(index, len(candidates)):
            stack.append(candidates[i])
            backtrack(i, stack, current_sum + candidates[i])
            stack.pop()

    backtrack(0, [], 0)
    return result
