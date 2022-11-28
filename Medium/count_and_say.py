# helper function that produces output string based on the previous string
def say(s: str) -> str:
    count = 1
    output = ""

    for i, c in enumerate(s):
        # if the current character is the same as the previous one, keep counting
        if i > 0 and s[i] == s[i - 1]:
            count += 1

        # if the current character is different from the previous one, stop counting that character and produce
        # partial output
        elif i > 0 and s[i] != s[i - 1]:
            output += str(count) + s[i - 1]
            count = 1
        # when we reach the end of the string, add the final count result
        if i == len(s) - 1:
            output += str(count) + s[i]

    return output


# recursively call the function n times
def count_and_say(n: int) -> str:
    if n == 1:
        return "1"
    return say(count_and_say(n - 1))
