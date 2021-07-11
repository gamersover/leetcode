import java.util.PriorityQueue;

class Solution {
    class Item implements Comparable<Item>{
        ListNode node;

        Item(ListNode node){
            this.node = node;
        }

        public int compareTo(Item item2){
            return this.node.val - item2.node.val;
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Item> pqueue = new PriorityQueue<Item>();
        for (ListNode node : lists){
            if(node != null) pqueue.offer(new Item(node));
        }
        ListNode fhead = new ListNode(0);
        ListNode curr = fhead;
        while (!pqueue.isEmpty()){
            Item item = pqueue.poll();
            curr.next = item.node;
            curr = curr.next;

            if(item.node.next != null) pqueue.offer(new Item(item.node.next));
        }
        return fhead.next;
    }
}