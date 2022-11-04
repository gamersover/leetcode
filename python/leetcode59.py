from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        max_layer = (n + 1) // 2
        ans = [[0]*n for _ in range(n)]
        number = 1
        for layer in range(max_layer):
            for i in range(layer, n-layer):
                ans[layer][i] = number
                number += 1
            for i in range(layer+1, n-layer):
                ans[i][n-layer-1] = number
                number += 1
            if len(ans) == n *n:
                return ans
            for i in range(n-layer-2, layer-1, -1):
                ans[n-layer-1][i] = number
                number += 1
            for i in range(n-layer-2, layer, -1):
                ans[i][layer] = number
                number += 1
        return ans


print(Solution().generateMatrix(4))