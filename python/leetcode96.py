class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for k in range(2, n+1):
            for i in range(k):
                dp[k] += dp[i]*dp[k-i-1]
        return dp[n]


print(Solution().numTrees(4))