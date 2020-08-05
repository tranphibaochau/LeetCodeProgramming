class WordDictionary:

    def __init__(self):
        self.trie ={}

    def addWord(self, word) -> None:
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = '#'

    def search(self, word):
        #recursively search when we encounter a '.'
        def search_in_node(word, t):
            for i, ch in enumerate(word):
                if not ch in t:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in t:
                            if x != '#' and search_in_node(word[i + 1:], t[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    t = t[ch]
            return '#' in t
        return search_in_node(word, self.trie) 
