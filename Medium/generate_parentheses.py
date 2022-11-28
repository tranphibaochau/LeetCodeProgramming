
def generate_parenthesis(n):
    result = []

    def backtrack(S, left, right):
        # when the string has n pairs of parentheses, return
        if len(S) == 2 * n:
            result.append("".join(S))
            return

        # recursively add "(" while possible
        if left < n:
            S.append("(")
            backtrack(S, left + 1, right)
            S.pop()
        # recursively add ")" as long as number of ")" is smaller than number of "("
        if right < left:
            S.append(")")
            backtrack(S, left, right + 1)
            S.pop()

    backtrack([], 0, 0)
    return result

print(generate_parenthesis(3))