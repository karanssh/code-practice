from typing import List

class TrieNode:
    def __init__(self):
        self.counts = 0 
        self.children = {}
        self.isEnd = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.counts += 1  # Move AFTER going to child node
        cur.isEnd = True

    def prefixCount(self, words: List[str], pref: str) -> int:
        cur = self.root
        for c in pref:
            if c not in cur.children:
                return 0
            cur = cur.children[c]
        return cur.counts  # Only return after full prefix match
    
sol = Solution()
words = ["pay","attention","practice","attend"]
for word in words:
    sol.addWord(word)

print(sol.prefixCount(words, "at"))  # 3
print(sol.prefixCount(words, "ba"))   # 3
print(sol.prefixCount(words, "bat"))  # 2
print(sol.prefixCount(words, "cat"))  # 0
