from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        max_layer = (min(m, n) + 1) // 2
        ans = []
        for layer in range(max_layer):
            for i in range(layer, n-layer):
                ans.append(matrix[layer][i])
            for i in range(layer+1, m-layer):
                ans.append(matrix[i][n-layer-1])
            if len(ans) == n * m:
                return ans
            for i in range(n-layer-2, layer-1, -1):
                ans.append(matrix[m-layer-1][i])
            for i in range(m-layer-2, layer, -1):
                ans.append(matrix[i][layer])
        return ans


print(Solution().spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]))


