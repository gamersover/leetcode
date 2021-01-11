#include<string>
#include<vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        int maxLen = 0;
        int start = 0, end = 0;
        vector<vector<int>> dp(n, vector<int>(n, false));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i; j < n; j++) {
                if (i == j) dp[i][j] = true;
                else if (s[i] == s[j]) {
                    if ((j - i) > 1) dp[i][j] = dp[i + 1][j - 1];
                    else dp[i][j] = true;
                }
                else
                    dp[i][j] = false;

                if (dp[i][j] && (j-i+1 > maxLen)) {
                    maxLen = max(j - i + 1, maxLen);
                    start = i;
                    end = j;
                }
            }
        }
        return s.substr(start, maxLen);
    }
};