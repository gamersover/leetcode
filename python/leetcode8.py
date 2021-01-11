class AtoiFSM:
    def __init__(self):
        self.state = "start"
        self.sign = 1
        self.val = 0
        self.table = {
                      #   space    +/-      0-9     other
            "start" :   ["start", "sign", "number", "end"],
            "sign"  :   ["end",   "end",  "number", "end"],
            "number":   ["end",   "end",  "number", "end"],
            "end"   :   ["end",   "end",  "end",    "end"], 
        }
    
    def _get_state_transfer_id(self, c):
        if c == " ":
            return 0
        elif c == "+" or c == "-":
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def run(self, c):
        # 状态转换
        self.state = self.table[self.state][self._get_state_transfer_id(c)]

        if self.state == "sign":
            self.sign = 1 if c == "+" else -1
        elif self.state == "number":
            self.val = self.val * 10 + int(c)
            self.val = min(self.val, 2**31-1) if self.sign == 1 else min(self.val, 2**31)
        elif self.state == "end":
            return self.sign * self.val
        return None


class Solution:
    def myAtoi(self, s):
        fsm = AtoiFSM()
        for c in s:
            res = fsm.run(c)
            if res is not None:
                return res
        return fsm.sign * fsm.val
