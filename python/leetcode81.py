from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)
        while left < right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                if nums[mid] < nums[right-1]:
                    right = mid
                elif nums[mid] > nums[right-1]:
                    if nums[right-1] < target:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    right -= 1
            else:
                if nums[mid] > nums[left]:
                    left = mid + 1
                elif nums[mid] < nums[left]:
                    if nums[left] > target:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    left += 1
        return False


print(Solution().search([2,5,6,0,0,1,2], 3))
