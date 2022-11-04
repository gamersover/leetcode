from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2):
            for i in range(layer, n-layer-1):
                t = matrix[layer][i]
                matrix[layer][i] = matrix[n-i-1][layer]
                matrix[n-i-1][layer] = matrix[n-layer-1][n-i-1]
                matrix[n-layer-1][n-i-1] = matrix[i][n-layer-1]
                matrix[i][n-layer-1] = t


m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(m)
print(m)