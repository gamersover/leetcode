#include<vector>
#include<string>

using namespace std;

class Solution {
vector<string> arr;
public:
    vector<string> generateParenthesis(int n) {
        generate(0, 0, "", n);
        return arr;
    }

    void generate(int left, int right, string s, int n){
        if(s.size() == 2 * n) {
            arr.push_back(s);
            return;
        }
        if(left < n){
            generate(left+1, right, s+"(", n);
        }
        if (right < left){
            generate(left, right+1, s+")", n);
        }
    }
};

