from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        right = len(nums) - 1
        left, curr = 0, 0
        while curr <= right:
            if nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1


arr = [2, 0, 1]
Solution().sortColors(arr)
print(arr)

