from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

    def suffixes(self, suffix=''):
        suffixes = []
        for char, node in self.children.items():
            if node.isWord:
                suffixes.append(suffix + char)
            if node.children:
                suffixes += node.suffixes(suffix + char)
        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def exists(self, word):
        node = self.find(word)
        return node.isWord if node else False

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


# ----------------------------------------------------------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------------------------------------------------------

trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    trie.insert(word)

# Find
assert type(trie.find("a")) is TrieNode
assert trie.find("b") is None

# Exists
assert trie.exists("ant") is True
assert trie.exists("tripod") is True
assert trie.exists("anthony") is False
assert trie.exists("bob") is False


# Suffixes
node = trie.find("a")
assert node.suffixes() == ["nt", "nthology", "ntagonist", "ntonym"]

node = trie.find("")
assert node.suffixes() == [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

node = trie.find("facto")
assert node.suffixes() == ["ry"]

node = trie.find("factory")
assert node.suffixes() == []
