from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for subres in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + subres)
        return res


print(Solution().permuteUnique([1,1,2]))