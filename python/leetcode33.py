from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                if nums[mid] > nums[left]:
                    if nums[left] <= target:
                        right = mid
                    else:
                        left = mid +1
                else:
                    right = mid
            elif nums[mid] < target:
                if nums[mid] > nums[left]:
                    left = mid + 1
                else:
                    if nums[right-1] >= target:
                        left = mid + 1
                    else:
                        right = mid
            else:
                return mid
        return -1


print(Solution().search([7, 8, 1, 2, 3, 4, 5, 6], 2))
