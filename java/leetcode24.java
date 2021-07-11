public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode fakeHead = new ListNode(0, head);
        ListNode curr = fakeHead;
        while ((curr.next != null) && (curr.next.next != null)) { 
            ListNode first = curr.next;
            ListNode second = first.next;
            first.next = second.next;
            second.next = first;
            curr.next = second;
            curr = first;
        }
        return fakeHead.next;
    }
}