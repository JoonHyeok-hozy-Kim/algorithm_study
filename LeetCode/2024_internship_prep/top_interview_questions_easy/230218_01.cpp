#include <unordered_set>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle_hashset(ListNode *head) {
        unordered_set<ListNode*> trace;
        ListNode* walk = head;
        while (walk) {
            if (trace.find(walk) == trace.end()){
                trace.insert(walk);
                walk = walk->next;
            } else {
                return true;
            }
        }
        return false;
    }
    
    bool hasCycle_inplace(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;
        
        if (slow == nullptr || slow->next == nullptr || fast->next->next == nullptr){
            return false;
        }
        
        slow = slow->next;
        fast = fast->next->next;
        
        while (fast->next && fast->next->next){
            if (slow == fast) return true;
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return false;
    }
};