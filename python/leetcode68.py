from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        start = 0
        while start < len(words):
            curr_len = len(words[start])
            end = start + 1
            while end < len(words) and curr_len + len(words[end]) + 1 <= maxWidth:
                curr_len += len(words[end]) + 1
                end += 1

            space_len = maxWidth - curr_len + (end - start - 1)
            if end == len(words):
                num_space, extra_space = 1, 0
            elif end - start - 1 == 0:
                num_space, extra_space = space_len, 0
            else:
                num_space = space_len // (end - start - 1)
                extra_space = space_len % (end - start - 1)

            res = ""
            if end - start - 1 == 0:
                res += words[start] + " " * (maxWidth - len(words[start]))
            else:
                for i in range(start, end):
                    res += words[i]
                    if i != end - 1:
                        res += " " * num_space
                        if extra_space > 0:
                            res += " "
                            extra_space -= 1
                res += " " * (maxWidth - len(res))
            ans.append(res)
            start = end
        return ans


if __name__ == "__main__":
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(Solution().fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
    print(Solution().fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))
