def one_edit_distance(s: str, t: str) -> bool:
    # if the difference in length between two strings is larger than 1, return False
    if abs(len(s) - len(t)) > 1:
        return False
    # boolean value to see if it's already one edit distance from each other
    edited = False
    i = j = 0
    while i < len(s) and j < len(t):
        # if there is more than one False comparisons, they are more than one edit distance away, return False
        if s[i] != t[j] and edited:
            return False
        # if there is a difference
        elif s[i] != t[j] and not edited:
            # if strings are of equal length, assume we modify one character and move on
            if len(s) == len(t):
                edited = True
            # if strings are of different length, skip the index of the longer string and move on
            elif len(s) > len(t):
                i += 1
                edited = True
                continue
            else:
                j += 1
                edited = True
                continue
        i += 1
        j += 1
    # if we did not reach the end of both string, return True if they are not yet one edit distance away, False if so
    if (i < len(s)) or (j < len(t)):
        return not edited
    # return whether the two strings are one edit distance away
    return edited

