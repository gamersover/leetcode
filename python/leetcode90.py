from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        start = len(res)
        res.append(res[0] + [nums[0]])
        end = len(res)
        for i in range(1, len(nums)):
            s = start if nums[i] == nums[i-1] else 0
            for j in range(s, end):
                res.append(res[j] + [nums[i]])
            start = end
            end = len(res)
        return res



print(Solution().subsetsWithDup([1, 2, 2]))