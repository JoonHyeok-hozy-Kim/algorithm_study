struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    bool deleted = false;
    
    int recursive(ListNode* curr, int n){
        int cnt;
        if (curr->next == nullptr){
            cnt = 1;
        } else {
            cnt = recursive(curr->next, n) + 1;
        }

        if (!deleted && cnt == n+1){
            ListNode* prev_next = curr->next;
            curr->next = prev_next->next;
            delete prev_next;
            deleted = true;
        }

        return cnt;
    }
    
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int recur_cnt = recursive(head, n);
        if (!deleted){
            ListNode* prev_head = head;
            head = head->next;
            delete prev_head;
        }
        
        return head;
    }
};