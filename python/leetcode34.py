from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) >> 1
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            if nums[left] == target:
                return left
            return -1

        def find_last(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) >> 1
                if nums[mid] <= target:
                    left = mid +1
                else:
                    right = mid

            if nums[left-1] == target:
                return left - 1
            return -1

        arr = [find_first(nums, target), find_last(nums, target)]
        return arr


print(Solution().searchRange([5,5 ], 5))