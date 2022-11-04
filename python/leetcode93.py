from typing import List


class Solution:
    def find_dots(self, s):
        dots = []
        for i in range(1, len(s)+1):
            if i == 1:
                dots.append(i)
            if i == 2 and s[0] != '0':
                dots.append(i)
            if i == 3 and ("100" <= s[:3] <= "255"):
                dots.append(i)
        return dots

    def restore(self, s, n):
        ans = []
        if n == 0:
            if len(s) == 0:
                ans.append("")
            return ans
        dots = self.find_dots(s)
        for dot in dots:
            subans = self.restore(s[dot:], n-1)
            for sub in subans:
                if sub == "":
                    ans.append(s[:dot])
                else:
                    ans.append(s[:dot] + "." + sub)
        return ans

    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restore(s, 4)



print(Solution().restoreIpAddresses("25525511135"))