#include <vector>

using namespace std;


class Solution {
public:
	void combination(vector< vector<int> >& res, vector<int>& candidates, vector<int> tmp, int target, int m) {
		if (target < 0)
			return;
		if (target == 0) {
			res.push_back(tmp);
		}
		for (int i = m; i < candidates.size(); i++) {
			tmp.push_back(candidates[i]);
			if (target - candidates[i] < 0)
				return;
			combination(res, candidates, tmp, target - candidates[i], i);
			tmp.pop_back();
		}
	}

	vector< vector<int> > combinationSum(vector<int>& candidates, int target) {
		if (candidates.size() == 0) {
			vector< vector<int> > res;
			return res;
		}
		vector< vector<int> > res;
		vector<int> tmp;
		sort(candidates.begin(), candidates.end());
		combination(res, candidates, tmp, target, 0);
		return res;
	}
};


int main(){
    vector<int> cans = {2, 3, 6, 7};
    Solution().combinationSum(cans, 7);
    return 0;
}