#include <unordered_set>
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
    struct TempResult{
        bool result;
        int min_val;
        int max_val;
    };
    
    TempResult _recursive(TreeNode* node){
        TempResult curr;
        curr.result = true;
        curr.min_val = node->val;
        curr.max_val = node->val;
        
        if (node->left){
            if (node->val == node->left->val){
                curr.result = false;
                return curr;
            }
            
            TempResult lefties = _recursive(node->left);
            if (!lefties.result) return lefties;
            
            if (lefties.min_val >= node->val || lefties.max_val >= node->val){
                curr.result = false;
                return curr;
            } else {
                curr.min_val = lefties.min_val;
            }
        }
        
        if (node->right){
            if (node->val == node->right->val){
                curr.result = false;
                return curr;
            }
            
            TempResult righties = _recursive(node->right);
            if (!righties.result) return righties;
            
            if (righties.min_val <= node->val || righties.max_val <= node->val){
                curr.result = false;
                return curr;
            } else {
                curr.max_val = righties.max_val;
            }
        }
        
        return curr;
    }
    
    
    bool isValidBST(TreeNode* root) {
        TempResult tr = _recursive(root);
        
        return tr.result;
    }
};