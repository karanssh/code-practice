class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = []  # Stores indices of words having this prefix/suffix


class WordFilter:
    def __init__(self, words: list[str]):
        # Two Tries: one for prefixes and one for suffixes
        self.prefix_root = TrieNode()
        self.suffix_root = TrieNode()
        
        for index, word in enumerate(words):
            self._insert(self.prefix_root, word, index)  # Insert word into the prefix Trie
            self._insert(self.suffix_root, word[::-1], index)  # Insert reversed word into the suffix Trie

    def _insert(self, root: TrieNode, word: str, index: int):
        current = root
        current.indices.append(index)  # Store the index of the word at the root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.indices.append(index)  # Store index in each node for efficient query lookup

    def _search(self, root: TrieNode, query: str) -> list[int]:
        current = root
        for char in query:
            if char not in current.children:
                return []  # No matching prefix/suffix
            current = current.children[char]
        return current.indices  # Get indices of matching words

    def f(self, pref: str, suff: str) -> int:
        # Search in prefix Trie for the prefix
        prefix_indices = self._search(self.prefix_root, pref)
        # Search in suffix Trie for the reversed suffix
        suffix_indices = self._search(self.suffix_root, suff[::-1])
        
        # Find largest common index
        prefix_indices = set(prefix_indices)
        suffix_indices = set(suffix_indices)
        common_indices = prefix_indices & suffix_indices
        return max(common_indices) if common_indices else -1


# Example usage:
wordFilter = WordFilter(["apple", "arcade", "arache"])
print(wordFilter.f("a", "e"))  # Output: 2