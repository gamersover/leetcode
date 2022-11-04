class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            elif len(p)>0 and p != ".":
                stack.append(p)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    print(Solution().simplifyPath("/home/"))
    print(Solution().simplifyPath("/a/./b/../../c/"))
    print(Solution().simplifyPath("/../"))
