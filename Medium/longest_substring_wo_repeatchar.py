"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.


"""
def lengthOfLongestSubstring(s):
    #start is the start of the sliding window [start, i)
    start = maxLength = 0
    usedChar = {}
    
    for i in range(len(s)):
         #if the character is used, and its position is after the start of the sliding window [start, i), slide start to just after i
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        #else slide i to the right and keep track of the largest length
        else:
            maxLength = max(maxLength, i - start + 1)
        #automatically record characters already in used and its position
        usedChar[s[i]] = i

    return maxLength