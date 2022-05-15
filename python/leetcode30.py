from typing import List




class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        num_words = len(words)
        total_len = num_words * word_len
        s_len = len(s)
        all_indices = []

        if s_len < total_len:
            return all_indices

        word_map = {}
        for word in words:
            word_map[word] = word_map.get(word, 0) + 1

        for wi in range(min(word_len, s_len - total_len+1)):
            start = curr = 0
            window_map = {}
            while wi + curr * word_len <= (s_len - word_len):
                curr_word = s[wi+curr*word_len:wi+curr*word_len+word_len]
                if curr_word not in word_map:
                    window_map = {}
                    start = curr + 1
                else:
                    window_map[curr_word] = [
                        window_map.get(curr_word, [0, []])[0] + 1,
                        window_map.get(curr_word, [0, []])[1] + [curr]
                    ]

                    if window_map[curr_word][0] > word_map[curr_word]:
                        new_start = window_map[curr_word][1][0] + 1
                        for i in range(start, window_map[curr_word][1][0] + 1):
                            window_map[s[wi+i*word_len:wi+i*word_len+word_len]][0] -= 1
                            window_map[s[wi+i*word_len:wi+i*word_len+word_len]][1].pop(0)
                        start = new_start

                    if curr - start + 1 == num_words:
                        if window_map[curr_word][0] == word_map[curr_word]:
                            all_indices.append(wi+start*word_len)
                        window_map[s[wi+start*word_len:wi+start*word_len+word_len]][0] -= 1
                        start += 1

                curr += 1
        return all_indices


s = "bcabbcaabbccacacbabccacaababcbb"
words = ["c","b","a","c","a","a","a","b","c"]
print(Solution().findSubstring(s, words))

