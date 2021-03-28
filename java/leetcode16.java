class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int first = 0;
        int closest = nums[0] + nums[1] + nums[2];
        while (first < nums.length - 2){
            int second = first + 1;
            int third = nums.length - 1;
            while (second < third){
                int s = nums[first] + nums[second] + nums[third];
                if (Math.abs(s - target) <= Math.abs(closest - target)){
                    closest = s;
                }
                if (closest == target) return target;
                if (s > target){
                    while ((third > second) && (nums[third] == nums[third-1])) third--;
                    third--;
                }
                else if (s < target){
                    while ((second < third) && (nums[second] == nums[second+1])) second++;
                    second++;
                }
            }
            while ((first < nums.length - 2) && (nums[first] == nums[first+1])) first++;
            first++;
        }
        return closest;
    }
}