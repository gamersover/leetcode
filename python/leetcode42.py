from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]*len(height)
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i])

        right = [height[-1]]*len(height)
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        area = 0
        for i in range(len(height)):
            area += min(left[i], right[i]) - height[i]
        return area
