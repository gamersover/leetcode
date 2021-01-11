#include<vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() < nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.size(), n = nums2.size();
        int halfLen = (m + n + 1) >> 1;
        int jleft = 0, jright = n;
        int i, j;
        while (jleft <= jright) {
            j = (jleft + jright) >> 1;
            i = halfLen - j;
            if (j < n && nums2[j] < nums1[i - 1])
                jleft = j + 1;
            else if (j > 0 && nums1[i] < nums2[j - 1])
                jright = j - 1;
            else break;
        }

        double max_left = 0, min_right = 0;
        if (j == 0) max_left = nums1[i - 1];
        else if (j == n && i == 0) max_left = nums2[j - 1];
        else max_left = max(nums1[i - 1], nums2[j - 1]);

        if ((m + n) % 2 == 1) return max_left;

        if (j == n) min_right = nums1[i];
        else if (j == 0 && i == m) min_right = nums2[j];
        else min_right = min(nums1[i], nums2[j]);

        return (min_right + max_left) / 2;
    }
};