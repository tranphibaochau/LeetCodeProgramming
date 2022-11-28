import copy


def word_break(s, word_dict):

    dp = [[] for i in range(len(s) + 1)]
    # mark the beginning of the dp array
    dp[0] = [-1]

    for i in range(len(dp)):
        # if we previously matched a word that ends at index i-1, find the next matched word(s)
        if len(dp[i]) != 0:

            for j in range(len(word_dict)):
                # a word has been matched
                if word_dict[j] == s[i:i + len(word_dict[j])]:
                    # if there exists a partial solution list, add the word just found onto the solution
                    if dp[i] != [-1]:
                        clone = copy.deepcopy(dp[i])
                        for n in clone:
                            n.append(word_dict[j])
                        dp[i + len(word_dict[j])].extend(clone)
                    # if we are at the start, create a list that contains the matched word
                    else:
                        dp[i + len(word_dict[j])].append([word_dict[j]])
    # join the matched words in the solution list at the final index into a string and return
    result = [" ".join([word for word in dp[-1][i]]) for i in range(len(dp[-1]))]
    return result
