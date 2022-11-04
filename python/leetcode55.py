from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_, i = 0, 0
        max_ = i + nums[i]
        while (i + 1) <= max_ and max_ < len(nums) - 1:
            i += 1
            if i <= max_:
                max_ = max(max_, i + nums[i])
            else:
                return False
        return max_ >= len(nums) - 1


print(Solution().canJump([3,1,1,1,4]))

