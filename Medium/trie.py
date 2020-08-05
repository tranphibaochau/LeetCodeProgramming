
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie ={}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        t = self.trie
        for c in word:
            
            if c not in t:
                t[c] = {}
            t = t[c]
        t['#'] = '#'
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        if '#' in t:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True

        


trie = Trie()
trie.insert("sup")
trie.insert("suppose")
trie.insert("what")
trie.insert("dafuq")
print(trie.search("sup"))
print(trie.search("fff"))
print(trie.startsWith("supp"))
print(trie.startsWith("www"))
print(trie.startsWith("why"))
print(trie.startsWith("ss"))