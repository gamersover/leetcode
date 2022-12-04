from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = dict()
        ans = 0
        for n in nums:
            if n not in dp:
                left = dp.get(n-1, 0)
                right = dp.get(n+1, 0)
                curr_len = left + right + 1
                if curr_len > ans:
                    ans = curr_len
                dp[n] = curr_len
                dp[n-left] = curr_len
                dp[n+right] = curr_len
        return ans


print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))