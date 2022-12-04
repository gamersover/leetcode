from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(i, -1, -1):
                if 0 < j < i:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                elif j == 0:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] += triangle[i-1][j-1]
        return min(triangle[n-1])


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Solution().minimumTotal(triangle)

