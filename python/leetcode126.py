from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        paths = [[beginWord]]  # BFS的结果
        level = 1 # BFS层数
        wordlist = set(wordList)  # BFS下一层可以使用的wordlist
        words = set() # BFS下一层使用过的words
        min_level = float("inf")  # 最小路径
        ans = [] # 最终结果
        alphabeta = [chr(i) for i in range(ord('a'), ord('a')+26)]

        if endWord not in wordlist:
            return ans

        # 特殊测试用例处理
        wordlist.discard(beginWord)

        while len(paths)>0:
            path = paths.pop(0)
            if len(path) > level: # 开始处理BFS下一层
                # 从wordlist中删除已经使用过的words
                for w in words:
                    wordlist.discard(w)
                words.clear()
                level = len(path) # 更新当前处理层数
                if level > min_level: # BFS层数已经超过最小路径，直接结束程序
                    break

            # 开始寻找path最后一个元素的相邻元素
            last = path[-1]
            for i in range(len(last)):
                for c in alphabeta:
                    new_last = last[:i] + c + last[i+1:]
                    if new_last not in wordlist:
                        continue
                    words.add(new_last)
                    new_path = path + [new_last]
                    if new_last == endWord:
                        ans.append(new_path)
                        min_level = level
                    else:
                        paths.append(new_path)
        return ans


print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))


