class Solution:
    def isNumber(self, s: str) -> bool:
        e_index = self.find_exp(s)
        if e_index == -1:
            return self.is_float(s)
        else:
            left, right = s[:e_index], s[e_index+1:]
            return self.is_float(left) and self.is_integer(right)

    def find_exp(self, s):
        for i, c in enumerate(s):
            if c == 'e' or c == 'E':
                return i
        return -1

    def is_digits(self, s):
        if len(s) == 0:
            return False
        for c in s:
            if c not in '0123456789':
                return False
        return True

    def is_integer(self, s):
        if len(s) == 0:
            return False
        if s[0] in ("+", "-"):
            s = s[1:]
        return self.is_digits(s)

    def is_float(self, s):
        if len(s) == 0:
            return False
        if s[0] in ("+", "-"):
            s = s[1:]
        dot_index = s.find(".")
        if dot_index == -1:
            return self.is_integer(s)
        else:
            int_, float_ = s[:dot_index], s[dot_index+1:]
            if len(int_) == 0:
                return self.is_digits(float_)
            elif len(float_) == 0:
                return self.is_integer(int_)
            else:
                return self.is_integer(int_) and self.is_digits(float_)


if __name__ == "__main__":
    print(Solution().isNumber("+.8"))