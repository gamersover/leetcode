class Solution:
    def match(self, schar, pchar):
        if pchar == ".":
            return True
        return pchar == schar

    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        # 空字符比较设为匹配，最终结果为dp[m][n]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    if i > 0 and self.match(s[i-1], p[j-1]):
                        dp[i][j] |= dp[i-1][j-1]
                else:
                    # 末位是'*'，则先与上`*`前面的字符不匹配`s`中字符的情况，
                    # 比如s=aa p=aaa*或s=ab p=abc*
                    dp[i][j] |= dp[i][j-2]
                    # 然后判断`s[i]`与`p[j-1]`匹配且`*`前面的字符匹配`s`中多个的情况
                    if i > 0 and self.match(s[i-1], p[j-2]):
                        dp[i][j] |= dp[i-1][j]
        return dp[m][n]
