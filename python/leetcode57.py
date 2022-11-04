from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        ans = []
        placed = False
        for first, second in intervals:
            if first > right:
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([first, second])
            elif second < left:
                ans.append([first, second])
            else:
                left = min(left, first)
                right = max(right, second)

        if not placed:
            ans.append([left, right])
        return ans


print(Solution().insert([[1,3],[6,9]], [2,5]))
