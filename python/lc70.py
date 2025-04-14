import unittest

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_small_cases(self):
        self.assertEqual(self.solution.climbStairs(1), 1)
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)
        self.assertEqual(self.solution.climbStairs(4), 5)

    def test_medium_case(self):
        self.assertEqual(self.solution.climbStairs(5), 8)
        self.assertEqual(self.solution.climbStairs(10), 89)

    def test_large_case(self):
        self.assertEqual(self.solution.climbStairs(30), 1346269)

if __name__ == "__main__":
    unittest.main()
