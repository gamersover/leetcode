from typing import List

class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            ans = max(ans, curr)
            if curr < 0:
                curr = 0
        return ans

    def maxSubArray(self, nums: List[int]) -> int:
        ans, curr = nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], curr+nums[i])
            ans = max(ans, curr)
        return ans

print(Solution().maxSubArray([5,4,-1,7,8]))

