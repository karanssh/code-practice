
def numDistinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: when t is empty, there's exactly one subsequence of s that matches it: the empty string
    for i in range(m + 1):
        dp[i][n] = 1

    # Fill the table from bottom up
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == t[j]:
                dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
            else:
                dp[i][j] = dp[i + 1][j]

    return dp[0][0]

# Example usage:
s1 = "rabbbit"
t1 = "rabbit"
print(numDistinct(s1,t1))  # Output: True