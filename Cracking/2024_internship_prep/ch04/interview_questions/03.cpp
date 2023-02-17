#include <iostream>
#include <vector>
#include <queue>
using namespace std;

template <typename T>
class ListNode{
    public:
        T data;
        ListNode *next = nullptr;

        ListNode(T t) : data(t) {};

        void print(){
            cout << this->data << " ";
            if (this->next != nullptr) this->next->print();
        }
};

template <typename T>
class TreeNode{
    public:
        T data;
        TreeNode *left = nullptr;
        TreeNode *right = nullptr;

        TreeNode(T t) : data(t) {};

        ListNode<T>* depth_list(ListNode<T>* last_node, int depth=0){
            last_node->next = new ListNode<T>(depth);
            last_node = last_node->next;
            if (this->left != nullptr){
                last_node = this->left->depth_list(last_node, depth+1);
            }
            if (this->right != nullptr){
                last_node = this->right->depth_list(last_node, depth+1);
            }
            return last_node;
        }
};

int main(){
    TreeNode<int>* t1 = new TreeNode<int>(1);
    t1->left = new TreeNode<int>(1);
    t1->right = new TreeNode<int>(1);

    ListNode<int>* l1 = new ListNode<int>(-1);
    t1->depth_list(l1);

    l1->print();
    cout << endl;

    TreeNode<int>* t2 = t1->right;
    for (int i=0; i<5; i++){
        t2->right = new TreeNode<int>(1);
        t2 = t2->right;
    }

    t1->depth_list(l1);
    l1->print();
}