import java.util.ArrayList;
import java.util.List;

class Solution {
    List<String> res = new ArrayList<>();
    public List<String> generateParenthesis(int n) {
        
        generate(n, 0, 0, "");
        return res;
    }

    void generate(int n, int left, int right, String s){
        if (s.length() == 2*n) {
            res.add(s);
            return;
        };
        
        if (left < n){
            generate(n, left+1, right, s+"(");
        }

        if (right < left){
            generate(n, left, right+1, s+")");
        }
    }
}