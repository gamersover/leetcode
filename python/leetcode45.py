from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_reach, max_reach, step = 0, 0, 0
        for i in range(len(nums)):
            if i > curr_reach:
                step += 1
                curr_reach = max_reach
            max_reach = max(max_reach, nums[i] + i)
        return step


print(Solution().jump([0]))
