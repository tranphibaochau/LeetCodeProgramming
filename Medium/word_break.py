def word_break(s, word_dict):
    # set up states for each character in the string
    dp = [False]*(len(s)+1)
    dp[0] = True

    for i in range(len(s)):
        # if we previously found a word in the dictionary that matches part of the string that starts at index i
        # record the match at index (i + len(word))
        if dp[i] is True:
            for j in range(len(word_dict)):
                if word_dict[j] == s[i:i+len(word_dict[j])]:
                    dp[i+len(word_dict[j])] = True
    # return the boolean stored in the final index
    return dp[-1]
