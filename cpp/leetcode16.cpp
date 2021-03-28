#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	int threeSumClosest(vector<int>& nums, int target) {
		sort(nums.begin(), nums.end());
		int first = 0;
		int closest = nums[0] + nums[1] + nums[2];
		while (first < nums.size() - 2) {
			int second = first + 1;
			int third = nums.size() - 1;
			while (second < third) {
				int s = nums[first] + nums[second] + nums[third];
				if (abs(s - target) <= abs(closest - target)) {
					closest = s;
					if (closest == target) return target;
				}
				if (s > target) {
					while((third > second) && (nums[third] == nums[third-1])) third--;
					third--;
				}
				else if(s < target) {
					while ((second < third) && (nums[second] == nums[second + 1])) second++;;
					second++;
				}
			}
			while ((first < nums.size() - 2) && (nums[first + 1] == nums[first])) first++;
			first++;
		}
		return closest;
	}
};