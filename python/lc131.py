from typing import List 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    dfs(end + 1, path)
                    path.pop()  # backtrack

        dfs(0, [])
        return res