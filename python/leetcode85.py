from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            matrix[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == '1':
                    matrix[i][j] = int(matrix[i-1][j]) + 1

        max_ = 0
        for i in range(m):
            max_ = max(self.largestRectangleArea(matrix[i]), max_)
        return max_

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(-1)
        max_ = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                if len(stack) == 0:
                    w = i
                else:
                    w = i - stack[-1] - 1
                max_ = max(max_, w * heights[j])

            stack.append(i)
        return max_