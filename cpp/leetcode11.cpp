#include<string>
#include<vector>
#include <algorithm>

using namespace std;


class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int i = 0, j = n - 1;
        int m = 0;
        while(i < j) {
            int cm = min(height[i], height[j]) * (j - i);
            m = cm > m ? cm : m;
            if (height[i] < height[j]) i++;
            else j--;
        }
        return m;
    }
};