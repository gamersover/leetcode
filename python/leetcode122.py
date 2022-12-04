from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0
        dp1 = -prices[0]
        for i in range(1, len(prices)):
            new_dp0 = max(dp0, dp1 + prices[i])
            new_dp1 = max(dp1, dp0 - prices[i])
            dp0, dp1 = new_dp0, new_dp1
        return dp0
