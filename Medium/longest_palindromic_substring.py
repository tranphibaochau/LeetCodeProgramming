#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#Example:

#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

def longestPalindrome(s):
        def helper(s, i, j): #if s[i:j+1] is a palindrome, check if s[i-1:j+2] is a palindrome until finding a longest palindrome centered around i
            if (j - i)%2 == 0 and i> 0 and (j < len(s)-1) and s[i-1] == s[j+1]:
                return helper(s, i-1, j+1)
            elif (j-i) %2 == 1 and i> 0 and (j < len(s)-1) and s[i-1] == s[j+1]:
                return helper(s, i-1, j+1)
            else:
                return s[i:j+1]
        max_r = ""
        r = ""
        for i, c in enumerate(s): #use dynamic programming to find the longest palindrome centered around each character, then return the maximum palindrome found
            if i < len(s)-1 and s[i] == s[i+1]:
                r = helper(s, i, i+1)
                if len(r) > len(max_r):
                    max_r = r

            r = helper(s, i, i)
            if len(r) > len(max_r):
                max_r = r
        return max_r