from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            for subres in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + subres)
        return res


print(Solution().permute([1,2,3]))