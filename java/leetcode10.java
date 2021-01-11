class Solution {
    private boolean match(char ch1, char ch2){
        if(ch2 == '.') return true;
        return ch1 == ch2;
    }
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m+1][n+1];
        
        dp[0][0] = true;
        for(int i=0; i<m+1; i++){
            for(int j=1; j<n+1; j++){
                if(p.charAt(j-1) != '*'){
                    if (i > 0 && match(s.charAt(i-1), p.charAt(j-1)))
                        dp[i][j] |= dp[i-1][j-1];
                }
                else{
                    dp[i][j] |= dp[i][j-2];
                    if (i > 0 && match(s.charAt(i-1), p.charAt(j-2)))
                        dp[i][j] |= dp[i-1][j];
                }
            }
        }
        return dp[m][n];
    }
}