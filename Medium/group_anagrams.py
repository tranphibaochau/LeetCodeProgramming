
def group_anagrams(strs):
    # function that returns a dictionary of character counts
    def count_chars(s):
        result = {}
        for c in s:
            if c not in result:
                result[c] = 1
            else:
                result[c] += 1
        return result
    # a dictionary with keys being the character counts of each string
    # keys are converted to str type so it can be hashed
    # and values being the list of strings with the same character count
    count_strs = {}
    for s in strs:
        # count the characters inside a string
        s_dict = count_chars(s)
        # get the list of characters in the string in alphabet order
        keys = sorted(s_dict.keys())
        # convert the dictionary into string format, by adding its count right after the character
        # Example: {'a': 1, "b": 2} -> "a1b2"
        new_key = ""
        for k in keys:
            new_key += k + str(s_dict[k])

        # group strings with the same character count into a list, using dictionary
        if new_key not in count_strs:
            count_strs[new_key] = [s]
        else:
            count_strs[new_key].append(s)
    return count_strs.values()


# solution using prime multiplication as the key
def group_anagrams(strs):

    primes = {'a': 2,
              'b': 3,
              'c': 5,
              'd': 7,
              'e': 11,
              'f': 13,
              'g': 17,
              'h': 19,
              'i': 23,
              'j': 29,
              'k': 31,
              'l': 37,
              'm': 41,
              'n': 43,
              'o': 47,
              'p': 53,
              'q': 59,
              'r': 61,
              's': 67,
              't': 71,
              'u': 73,
              'v': 79,
              'w': 83,
              'x': 89,
              'y': 97,
              'z': 101
              }

    strs_dict = {}

    for s in strs:
        product = 1

        for c in s:
            product *= primes[c]

        if product in strs_dict:
            strs_dict[product].append(s)
        else:
            strs_dict[product] = [s]

    return strs_dict.values()
