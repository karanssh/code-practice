class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Base cases
        for i in range(m+1):
            dp[i][n] = m - i  # Delete all remaining from word1
        for j in range(n+1):
            dp[m][j] = n - j  # Insert all remaining from word2

        # Bottom-up fill
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i+1][j],    # delete
                        dp[i][j+1],    # insert
                        dp[i+1][j+1],  # replace
                    )

        return dp[0][0]

if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))  # Output: 3