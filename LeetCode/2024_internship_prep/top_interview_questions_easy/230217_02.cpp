#include <iostream>
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
    bool isPalindrome(ListNode* head) {
        int size = 0;
        ListNode *slow = head;
        ListNode *fast = head;
        ListNode *slow_next;
        // ListNode* prev = new ListNode();
        
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
                
        ListNode *prev;
        slow_next = slow->next;
        slow->next = nullptr;
        prev = slow;
        slow = slow_next;
        while (slow){
            slow_next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = slow_next;
        }
        
        fast = head;
        while (prev){
            if (fast->val != prev->val) return false;
            prev = prev->next;
            fast = fast->next;
        }
        
        return true;
    }
};

int main(){
    ListNode l1(1);
    ListNode *walk = &l1;
    walk->next = new ListNode(2);
    walk = walk->next;
    walk->next = new ListNode(3);
    walk = walk->next;
    walk->next = new ListNode(2);
    walk = walk->next;
    walk->next = new ListNode(1);
    walk = walk->next;

    walk = &l1;
    // while (walk != nullptr){
    //     cout << walk->val << " ";
    //     walk = walk->next;
    // }

    Solution s1;
    cout << boolalpha << s1.isPalindrome(walk);
}