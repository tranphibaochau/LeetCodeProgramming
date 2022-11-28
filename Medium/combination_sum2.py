"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
"""
def combination_sum2(candidates, target):
    # it's important to sort the candidates so we can skip duplicate results later on
    candidates.sort()
    result = []

    def backtrack(index, stack, current_sum):
        if current_sum == target:
            # add the solution to the final list
            result.append(list(stack))
            return
        if current_sum > target:
            return
        for i in range(index, len(candidates)):
            # once a solution has been found, we will skip duplicated numbers
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            stack.append(candidates[i])
            # add the next number in the list until current_sum equals or exceeds the target
            backtrack(i + 1, stack, current_sum + candidates[i])
            stack.pop()

    backtrack(0, [], 0)
    return result
