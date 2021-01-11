class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        int maxLen = 0;
        int start = 0, end = 0;
        Boolean[][] dp = new Boolean[n][n];
        for(int i=n-1; i>=0; i--) {
            for(int j=i; j<n; j++) {
                if(i == j) dp[i][j] = true;
                else if(s.charAt(i) == s.charAt(j)){
                    if(j - i > 1) dp[i][j] = dp[i+1][j-1];
                    else dp[i][j] = true;
                }
                else dp[i][j] = false;

                if (dp[i][j] && ((j - i + 1) > maxLen)){
                    maxLen = j - i + 1;
                    start = i;
                    end = j;
                }
            }
        }
        return s.substring(start, end+1);
    }
}