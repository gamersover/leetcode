from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for e in nums:
            n = len(ans)
            for i in range(n):
                ans.append(ans[i].copy() + [e])
        return ans


print(Solution().subsets([1, 2, 3]))
