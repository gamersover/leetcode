#include<string>
#include<vector>
#include<unordered_map>
#include <algorithm>

using namespace std;

class AtoiFSM {
    string state = "start";
    unordered_map<string, vector<string>> map = {
        {"start", {"start", "sign", "number", "end"} },
        {"sign", {"end",   "end",  "number", "end"}},
        {"number", {"end",   "end",  "number", "end"}},
        {"end", {"end",   "end",  "end", "end"}}
    };
public:
    long long val = 0;
    int sign = 1;
    
    int get_state_transfer_id(char c) {
        if (c == ' ') return 0;
        else if (c == '+' || c == '-') return 1;
        else if (isdigit(c)) return 2;
        return 3;
    }

    void run(char c) {
        state = map[state][get_state_transfer_id(c)];
        if (state == "sign") sign = c == '+' ? 1 : -1;
        else if (state == "number") {
            val = val * 10 + c - '0';
            val = sign == 1 ? min(val, (long long) INT_MAX) : min(val, - (long long) INT_MIN);
        }
    }
};

class Solution {
public:
    int myAtoi(string str) {
        AtoiFSM fsm = AtoiFSM();
        for (auto c : str) {
            fsm.run(c);
        }
        return (int)(fsm.sign * fsm.val);
    }
};