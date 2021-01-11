import java.util.HashMap;
import java.util.Map;

class AtoiFSM {
    private String state = "start";
    public int sign = 1;
    public long val = 0;
    private Map<String, String[]> table = new HashMap<>();

    public AtoiFSM() {
        table.put("start", new String[]{"start", "sign", "number", "end"});
        table.put("sign", new String[]{"end", "end", "number", "end"});
        table.put("number", new String[]{"end", "end", "number", "end"});
        table.put("end", new String[]{"end", "end", "end", "end"});
    }

    private int getStateTransferID(char c){
        if (c == ' ') {
            return 0;
        }
        else if (c == '+' || c == '-') {
            return 1;
        }
        else if (Character.isDigit(c)){
            return 2;
        }
        return 3;
    }

    public void run(char c){
        state = table.get(state)[getStateTransferID(c)];
        if (state.equals("sign")) {
            sign = c == '+' ? 1 : -1;
        }
        else if (state.equals("number")){
            val = val * 10 + c - '0';
            val = sign == 1 ? Math.min(val, Integer.MAX_VALUE) : Math.min(val, - (long) Integer.MIN_VALUE);
        }
    }
}


class Solution {
    private AtoiFSM fsm = new AtoiFSM();
    public int myAtoi(String s) {
        for(int i = 0; i < s.length(); i++){
            fsm.run(s.charAt(i));
        }
        return (int) (fsm.sign * fsm.val);
    }
}