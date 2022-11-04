class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_map = dict()
        for c in t:
            cnt_map[c] = cnt_map.get(c, 0) + 1

        substr = ""
        min_len = len(s) + 1
        cnt, j = 0, 0
        window_cnt_map = dict()
        for i, ch in enumerate(s):
            window_cnt_map[ch] = window_cnt_map.get(ch, 0) + 1

            if ch in cnt_map and window_cnt_map[ch] <= cnt_map[ch]:
                cnt += 1

            while j <= i and (s[j] not in cnt_map or window_cnt_map[s[j]] > cnt_map[s[j]]):
                window_cnt_map[s[j]] -= 1
                j += 1

            if cnt == len(t):
                if i - j + 1 < min_len:
                    min_len = i - j + 1
                    substr = s[j:i+1]
        return substr


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
