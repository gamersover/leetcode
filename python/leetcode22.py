class Solution:
    def generateParenthesis(self, n):
        self.n = n
        self.result = []
        self.generate(0, 0)
        return self.result

    def generate(self, left, right, s=""):
        if len(s) == self.n * 2:
            self.result.append(s)
            return 
        
        if left < self.n:
            self.generate(left+1, right, s+"(")
        
        if right < left:
            self.generate(left, right+1, s+")")
        

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
