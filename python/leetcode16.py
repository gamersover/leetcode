class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = sum(nums[:3])
        first = 0
        while first < len(nums) - 2:
            second, third = first + 1, len(nums) - 1
            while second < third:
                s = nums[first] + nums[second] + nums[third]
                if abs(s - target) <= abs(closest - target):
                    closest = s
                    if closest == target:
                        return target
                if s > target:
                    while third > second and nums[third] == nums[third-1]:
                        third -= 1
                    third -= 1
                elif s < target:
                    while second < third and nums[second] == nums[second+1]:
                        second += 1
                    second += 1
            
            while first < len(nums) - 2 and nums[first] == nums[first+1]:
                first += 1
            first += 1
        
        return closest
