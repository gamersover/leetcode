from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabeta = [chr(i) for i in range(ord('a'), ord('a')+26)]
        word_list = set(wordList)
        level_arr = [beginWord]     # BFS当前层元素
        visited = set([beginWord])
        res = 0
        while len(level_arr) > 0:
            res += 1
            level_len = len(level_arr)
            while level_len > 0:    # 处理完当前层所有元素
                s = level_arr.pop(0)
                for i in range(len(s)):
                    for c in alphabeta:
                        new_s = s[:i] + c + s[i+1:]
                        if new_s in word_list and new_s == endWord:
                            return res + 1
                        if new_s not in word_list or new_s in visited:
                            continue
                        level_arr.append(new_s)
                        visited.add(new_s)
                level_len -= 1
        return 0
