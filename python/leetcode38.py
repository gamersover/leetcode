class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            new_s = ""
            for i in range(len(s)):
                if i == 0:
                    curr = s[i]
                    curr_cnt = 1
                else:
                    if s[i] == curr:
                        curr_cnt += 1
                    else:
                        new_s += str(curr_cnt) + str(curr)
                        curr = s[i]
                        curr_cnt = 1
            new_s += str(curr_cnt) + str(curr)
            s = new_s
        return s


print(Solution().countAndSay(5))

