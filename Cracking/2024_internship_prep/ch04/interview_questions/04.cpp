#include <iostream>
#include <exception>
using namespace std;

template <typename T>
class TreeNode{
    public:
        T data;
        TreeNode *left = nullptr;
        TreeNode *right = nullptr;

        TreeNode(T t) : data(t) {};

        struct CheckResult{
            bool result;
            int depth_cnt;
        };

        CheckResult _check_balanced(int depth=0){
            int left_depth, right_depth;

            if (this->left == nullptr){
                left_depth = depth;
            } else {
                CheckResult cr1 = this->left->_check_balanced(depth+1);
                if (!cr1.result) return cr1;
                else left_depth = cr1.depth_cnt;
            }

            if (this->right == nullptr){
                right_depth = depth;
            } else {
                CheckResult cr2 = this->right->_check_balanced(depth+1);
                if (!cr2.result) return cr2;
                else right_depth = cr2.depth_cnt;
            }

            CheckResult cr3;
            int diff = left_depth - right_depth;
            if (diff == 0 || diff == -1 || diff == 1){
                cr3.result = true;
                if (left_depth > right_depth) cr3.depth_cnt = left_depth;
                else cr3.depth_cnt = right_depth;
            } else {
                cr3.result = false;
                cr3.depth_cnt = 0;
            }
            return cr3;
        }

        bool check_balanced(){
            CheckResult cr = _check_balanced();
            return cr.result;
        }
};


int main(){
    TreeNode<int>* t1 = new TreeNode<int>(1);
    t1->left = new TreeNode<int>(1);
    t1->right = new TreeNode<int>(1);

    cout << boolalpha << t1->check_balanced() << endl;

    TreeNode<int>* t2 = t1->right;
    for (int i=0; i<1; i++){
        t2->right = new TreeNode<int>(1);
        t2 = t2->right;
    }

    cout << boolalpha << t1->check_balanced() << endl;
    for (int i=0; i<1; i++){
        t2->right = new TreeNode<int>(1);
        t2 = t2->right;
    }

    cout << boolalpha << t1->check_balanced() << endl;

    t1->left->left = new TreeNode<int>(1);

    cout << boolalpha << t1->check_balanced() << endl;

    t1->right->left = new TreeNode<int>(1);

    cout << boolalpha << t1->check_balanced() << endl;
}