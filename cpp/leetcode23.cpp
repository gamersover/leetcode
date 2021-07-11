#include <vector>
#include <queue>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
	struct Item {
		ListNode *node;
		bool operator < (const Item &item) const {
			return node->val > item.node->val;
		}
	};
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		priority_queue<Item> plist;
		for (auto node : lists) {
			if (node) plist.push({ node });
		}
		ListNode fhead, *curr = &fhead;
		while (!plist.empty()) {
			auto item = plist.top();
			plist.pop();
			curr->next = item.node;
			curr = curr->next;
			if (item.node->next) plist.push({ item.node->next });
		}
		return fhead.next;
	}
};