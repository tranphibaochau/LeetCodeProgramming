"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""

def countCharacters(words, chars):
    res = 0
    for word in words:
        matched = True
        for i in word:
            if word.count(i) > chars.count(i):
                matched = False
                break
        if matched:
            res += len(word)
    return res