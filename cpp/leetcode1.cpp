#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            auto j = map.find(target - nums[i]);
            if (j != map.end()) {
                return {j->second, i};
            }
            else
                map[nums[i]] = i;
        }
        return {};
    }
};