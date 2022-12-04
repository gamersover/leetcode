from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0, 0] for i in range(k+1)]
        for i in range(0, k+1):
            dp[i][0] = 0
            dp[i][1] = -prices[0]

        n = len(prices)
        for i in range(n):
            for j in range(1, k+1):
                new_dp0 = max(dp[j][0], dp[j][1] + prices[i])
                new_dp1 = max(dp[j][1], dp[j-1][0] - prices[i])
                dp[j][0] = new_dp0
                dp[j][1] = new_dp1
        return dp[k][0]


k = 3
prices = [3,2,6,5,0,3]
print(Solution().maxProfit(k, prices))