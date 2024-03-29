from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell1, sell2 = 0, 0
        buy1, buy2 = -prices[0], -prices[0]
        for i in range(1, len(prices)):
            sell2 = max(sell2, buy2 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy1 = max(buy1, -prices[i])
        return sell2


print(Solution().maxProfit([1, 9]))
