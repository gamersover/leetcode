struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
	ListNode* swapPairs(ListNode* head) {
		ListNode* fakeHead = new ListNode(0, head);
		ListNode* curr = fakeHead;
		while ((curr->next != NULL) && (curr->next->next != NULL)) {
			ListNode* first = curr->next;
			ListNode* second = first->next;
			first->next = second->next;
			second->next = first;
			curr->next = second;
			curr = first;
		}
		return fakeHead->next;
	}
};