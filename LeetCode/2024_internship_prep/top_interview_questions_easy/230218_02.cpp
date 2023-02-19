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
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        
        int curr_depth = 1;
        int left_depth = 0;
        int right_depth = 0;
        
        if (root->left) {
            left_depth = maxDepth(root->left);
            if (curr_depth < left_depth + 1) curr_depth = left_depth + 1;
        }
        
        
        if (root->right) {
            right_depth = maxDepth(root->right);
            if (curr_depth < right_depth + 1) curr_depth = right_depth + 1;
        }
        
        
        return curr_depth;
    }
};