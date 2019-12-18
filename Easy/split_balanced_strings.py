####################################################################################################################
#Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#Given a balanced string s split it in the maximum amount of balanced strings.
#Return the maximum amount of splitted balanced strings.
#
#Example: 
#Input: s = "RLRRLLRLRL"
#Output: 4
#Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
#
####################################################################################################################
from itertools import accumulate

#solution using iteration:
# 1. set a flag to zero and loop through characters in string;
# 2. if char is R, add flag by 1; if char is L, subtract 1 from flag
# 3. add 1 to counter whenever flag is 0.
def balancedStringSplit(s):
    return list(accumulate(1 if c == "R" else -1 for c in s)).count(0)

print(balancedStringSplit("RRRLLLRLRL"))

#Solution using recursion
def balancedStringSplit(s, n=0):
    def checkBalance(m, n):
        substring = m[0:n]
        if substring.count('L') == substring.count('R'):
            return True
        return False
    if (len(s) == 0) or (n >= len(s)):
        return 0
    elif checkBalance(s, n+2):
        return 1 + balancedStringSplit(s[n+2:], 0)
    else:
        return balancedStringSplit(s, n+2)
print(balancedStringSplit("RRRLLLRLRL"))