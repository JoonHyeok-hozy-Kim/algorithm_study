#include <iostream>
#include <queue>
using namespace std;

template <typename T>
class TreeNode{
    public:
        T data;
        TreeNode* left = nullptr;
        TreeNode* right = nullptr;

        TreeNode(T t) : data(t) {};
        ~TreeNode(){
            if (this->left) delete left;
            if (this->right) delete right;
        }

        friend ostream& operator<<(ostream&os, const TreeNode& tn){
            os << "[" << tn.data << "]";
            return os;
        }

        bool check_subtree(TreeNode* other){
            queue<TreeNode*> Q;
            Q.push(this);
            while (!Q.empty()){
                if (Q.front() == other) return true;

                if (Q.front()->left) Q.push(Q.front()->left);
                if (Q.front()->right) Q.push(Q.front()->right);
                Q.pop();
            }
            return false;
        }
};

int main(){
    TreeNode<int> *t1 = new TreeNode<int>(4);
    t1->left = new TreeNode<int>(2);
    t1->right = new TreeNode<int>(6);
    t1->left->left = new TreeNode<int>(1);
    t1->left->right = new TreeNode<int>(3);
    t1->right->left = new TreeNode<int>(5);
    t1->right->right = new TreeNode<int>(7);
    cout << boolalpha << t1->check_subtree(t1->right->right) << endl;
    
    TreeNode<int>* t2 = new TreeNode<int>(10);
    cout << boolalpha << t1->check_subtree(t2) << endl;

}