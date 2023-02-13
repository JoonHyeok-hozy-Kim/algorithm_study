#include <iostream>
#include <exception>
#include <vector>
#include <algorithm>
#include <random>
using namespace std;

template <typename T>
class TreeNode {
    public:
        T data;
        TreeNode<T> *parent = nullptr;
        TreeNode<T> *left = nullptr;
        TreeNode<T> *right = nullptr;

        TreeNode(T t) : data(t) {};
        TreeNode(T t, TreeNode<T> *parent_node) : data(t), parent(parent_node) {};
        ~TreeNode() {
            if (this->left != nullptr) delete this->left;
            if (this->right != nullptr) delete this->right;
            cout << "Node(" << this->data << ") deleted." << endl;
        };

        TreeNode<T>* add_left(T t){
            TreeNode<T> *left_node = new TreeNode<T>(t, this);
            this->left = left_node;
            return left_node;
        }

        TreeNode<T>* add_right(T t){
            TreeNode<T> *right_node = new TreeNode<T>(t, this);
            this->right = right_node;
            return right_node;
        }

        void swap(TreeNode<T> *other){
            T temp = this->data;
            this->data = other->data;
            other->data = temp;
        }
};


template <typename T>
class Heap{
    public:
        TreeNode<T> *root = nullptr;
        TreeNode<T> *tail = nullptr;

        bool is_empty() {
            return root == nullptr;
        }

        T top(){
            if (this->is_empty()) throw exception();
            return this->root->data;
        }

        TreeNode<T>* up_heap(TreeNode<T> *target){
            while (target->parent != nullptr && target->parent->data < target->data){
                target->swap(target->parent);
                target = target->parent;
            }
        }

        TreeNode<T>* down_heap(TreeNode<T> *target){
            TreeNode<T> *next;
            while (1){
                next = nullptr;
                if (target->left != nullptr && target->left->data > target->data){
                    next = target->left;
                } else if (target->right != nullptr && target->right->data > target->data){
                    next = target->right;
                }

                if (next != nullptr){
                    target->swap(next);
                    target = next;                    
                } else {
                    break;
                }
            }
        }

        void push(T t){
            if (this->is_empty()){
                TreeNode<T> *new_root = new TreeNode<T>(t);
                this->root = new_root;
                this->tail = new_root;
            }
        }

        void pop(){

        }
};


int main(){
    vector<int> v1;
    random_device rd;
    mt19937 generator_obj(rd());
    uniform_int_distribution<int> dist_obj(0, 99);
    for (int i=0; i<10; i++){
        v1.push_back(dist_obj(generator_obj));
    }

    cout << "[ ";
    for (int c : v1) cout << c << " ";
    cout << "]\n";

    make_heap(v1.begin(), v1.end());
    cout << "[ ";
    for (int c : v1) cout << c << " ";
    cout << "]\n";
}