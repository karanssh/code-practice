

# A rotation group for a string contains all of its unique rotations. For example, "123" can be rotated to "231" and "312" and they are all in the same rotation group.

# Given a list of strings words, group each word by their rotation group, and return the total number of groups.

# Constraints

#     n ≤ 200 where n is the length of words.




class Solution:
    def solve(self, words):
        s = set()
        ans = 0
        for w in words:
            if w not in s:
                ans += 1
            for i in range(len(w)):
                s.add(w[i:] + w[:i])
        return ans
        