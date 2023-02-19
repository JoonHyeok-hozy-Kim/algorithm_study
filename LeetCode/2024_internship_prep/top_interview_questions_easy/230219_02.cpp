#include <unordered_set>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!(root->left) && !(root->right)) return true;
        else if ((root->left && !(root->right)) || !(root->left) && root->right) return false;
        
        TreeNode *left_popped, *right_popped;
        queue<TreeNode*> q_left;
        queue<TreeNode*> q_right;
        
        q_left.push(root->left);
        q_right.push(root->right);
        
        while (!q_left.empty() && !q_right.empty()){
            left_popped = q_left.front();
            right_popped = q_right.front();
            q_left.pop();
            q_right.pop();
            
            if (left_popped->val != right_popped->val) return false;
            
            if ((left_popped->left && !(right_popped->right)) ||
                (!(left_popped->left) && right_popped->right)) return false;
            else if (left_popped->left && right_popped->right){
                q_left.push(left_popped->left);
                q_right.push(right_popped->right);
            }
                        
            if ((left_popped->right && !(right_popped->left)) ||
                (!(left_popped->right) && right_popped->left)) return false;
            else if (left_popped->right && right_popped->left){
                q_left.push(left_popped->right);
                q_right.push(right_popped->left);
            }
        }
        
        return true;
    }
};