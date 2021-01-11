#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    bool match(char ch1, char ch2) {
        if (ch2 == '.') return true;
        return ch1 == ch2;
    }
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, false));
        dp[0][0] = true;
        for (int i = 0; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] != '*') {
                    if (i > 0 && match(s[i - 1], p[j - 1]))
                        dp[i][j] |= dp[i - 1][j - 1];
                }
                else {
                    dp[i][j] |= dp[i][j - 2];
                    if (i > 0 && match(s[i - 1], p[j - 2]))
                        dp[i][j] |= dp[i - 1][j];
                }
            }
        }
        return dp[m][n];
    }
};