class TrieNode:
    def __init__(self, c, is_end=False):
        self.char = c
        self.is_end = is_end
        self.children = {}
class Trie(object):
    """A trie has at least the root node, the root node doesn't store any character"""
    def __init__(self):
        self.trie = {}
    def insert(self, word):
        """insert a word to the tree"""
        # start at the root node, then traverse down to find each character of the word to see if it has been inserted
        node = self.trie

        for c in word:
            if c not in node:
                node[c] = Trie()
            node = node[c]
        node['#']

trie = Trie()
trie.insert("whatthehell")
trie.insert("whatever")