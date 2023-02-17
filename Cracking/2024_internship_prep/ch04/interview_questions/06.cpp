#include <iostream>
using namespace std;

template <typename T>
class TreeNode{
    public:
        T data;
        TreeNode* parent = nullptr;
        TreeNode* left = nullptr;
        TreeNode* right = nullptr;

        TreeNode(T t) : data(t) {};
        TreeNode(T t, TreeNode* parent_node) : data(t), parent(parent_node) {};
        ~TreeNode() {
            if (this->left) delete this->left;
            if (this->right) delete this->right;
        }

        TreeNode* drill_down_left(){
            TreeNode* result = this;
            while (result->left){
                result = result->left;
            }
            return result;
        }

        TreeNode* successor(){
            TreeNode* result;
            if (this->right){
                result = this->right->drill_down_left();
            } else if (this->parent->left == this){
                result = this->parent;
            } else {
                result = this;
                while (result->parent){
                    result = result->parent;
                    if (result == result->parent->left){
                        result = result->parent;
                        break;
                    } else if (result->parent == nullptr){
                        return nullptr;
                    }
                }
            }

            return result;
        }
};

int main(){
    TreeNode<int>* t1 = new TreeNode<int>(4);
    t1->left = new TreeNode<int>(2, t1);
    t1->left->left = new TreeNode<int>(1, t1->left);
    t1->left->right = new TreeNode<int>(3, t1->left);
    t1->right = new TreeNode<int>(6, t1);
    t1->right->left = new TreeNode<int>(5, t1->right);
    t1->right->right = new TreeNode<int>(7, t1->right);

    t1 = t1->left->left;
    while (t1 != nullptr){
        cout << t1->data << " ";
        t1 = t1->successor();
    }
}