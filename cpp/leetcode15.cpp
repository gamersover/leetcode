#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        if (nums.size() < 3) return {};
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size() - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int left = i + 1;
            int right = nums.size() - 1;
            while (left < right) {
                if (nums[left] + nums[right] > -nums[i]) right--;
                else if (nums[left] + nums[right] < -nums[i]) left++;
                else {
                    res.push_back({nums[i], nums[left], nums[right]});
                    while ((left < right) && (nums[left] == nums[left+1])) left++;
                    while ((left < right) && (nums[right] == nums[right-1])) right--;
                    left++; right--;
                }
            }
        }
        return res;
    }
};