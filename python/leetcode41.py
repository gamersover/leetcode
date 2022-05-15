from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = len(nums) - 1
        while i >= 0:
            if 0  <= nums[i] - 1 < len(nums) and nums[nums[i]-1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i -= 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


print(Solution().firstMissingPositive([3, 4, -1, 1]))

