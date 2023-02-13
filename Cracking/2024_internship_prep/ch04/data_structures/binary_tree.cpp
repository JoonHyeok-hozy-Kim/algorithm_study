#include <iostream>
#include <exception>
#include <queue>
using namespace std;

template <typename T>
class TreeNode {
    public:
        T data;
        TreeNode<T> *left = nullptr;
        TreeNode<T> *right = nullptr;

        TreeNode(T t) : data(t) {};
        ~TreeNode() {
            if (this->left != nullptr) delete this->left;
            if (this->right != nullptr) delete this->right;
            cout << "Node(" << this->data << ") deleted." << endl;
        };

        TreeNode<T>* add_left(T t){
            TreeNode<T> *left_node = new TreeNode<T>(t);
            this->left = left_node;
            return left_node;
        }

        TreeNode<T>* add_right(T t){
            TreeNode<T> *right_node = new TreeNode<T>(t);
            this->right = right_node;
            return right_node;
        }

        void preorder_traversal(){
            cout << this->data << " ";
            if (this->left != nullptr) this->left->preorder_traversal();
            if (this->right != nullptr) this->right->preorder_traversal();
        }

        void inorder_traversal(){
            if (this->left != nullptr) this->left->inorder_traversal();
            cout << this->data << " ";
            if (this->right != nullptr) this->right->inorder_traversal();
        }

        void postorder_traversal(){
            if (this->left != nullptr) this->left->postorder_traversal();
            if (this->right != nullptr) this->right->postorder_traversal();
            cout << this->data << " ";
        }

        void breadth_first_traversal(){
            queue<TreeNode<T>*> Q;
            TreeNode<T> *curr;
            Q.push(this);
            while (!Q.empty()){
                curr = Q.front();
                Q.pop();
                cout << curr->data << " ";
                if (curr->left != nullptr) Q.push(curr->left);
                if (curr->right != nullptr) Q.push(curr->right);
            }
        }
};

int main() {
    TreeNode<int> T1(0);
    TreeNode<int> *left = T1.add_left(1);
    left->add_left(2);
    left->add_right(3);
    TreeNode<int> *right = T1.add_right(4);
    right->add_left(5);
    right->add_right(6);

    T1.preorder_traversal();
    cout << endl;
    T1.inorder_traversal();
    cout << endl;
    T1.postorder_traversal();
    cout << endl;
    T1.breadth_first_traversal();
    cout << endl;
}