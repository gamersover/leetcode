from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m
        while left < right:
            mid = left + ((right - left) >> 1)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid

        nrow = left - 1
        left, right = 0, n
        while left < right:
            mid = left + ((right - left) >> 1)
            if matrix[nrow][mid] == target:
                return True
            elif matrix[nrow][mid] < target:
                left = mid + 1
            else:
                right = mid
        return False


print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))