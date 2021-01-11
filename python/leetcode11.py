class Solution:
    def maxArea(self, height):
        n = len(height)
        i, j = 0, n-1
        m = 0
        while i < j:
            m = max(m, min(height[j], height[i]) * (j - i))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m
