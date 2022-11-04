from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n+1)]
        else:
            ans = []
            for i in range(n, k-1, -1):
                for arr in self.combine(i-1, k-1):
                    ans.append(arr + [i])
            return ans


print(Solution().combine(4, 2))