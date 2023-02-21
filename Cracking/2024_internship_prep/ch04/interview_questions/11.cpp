#include <iostream>
using namespace std;

template <typename T>
class Tree{
    protected:
        class Node{
            public:
                T data;
                Node* parent = nullptr;
                Node* left = nullptr;
                Node* right = nullptr;

                Node(T t) : data(t) {};
                Node(T t, Node* p) : data(t), parent(p) {};
                ~Node() {
                    if (this->left) delete this->left;
                    if (this->right) delete this->right;
                }

                friend ostream& operator<<(ostream& os, const Node &n){
                    os << "[" << n.data << "]";
                    return os;
                }
            };
            Node* root = nullptr;
            int size = 0;
    
    public:

        Tree() {};
        ~Tree() { if (this->root) delete root; }

        Node* get_root(){
            return this->root;
        }

        int get_size(){
            return this->size;
        }

        Node* set_root(T t){
            if (this->root) throw exception();
            this->root = new Node(t);
            this->size++;
            return this->root;            
        }

        Node* add_left(Node* parent, T t){
            if (parent->left) throw exception();
            parent->left = new Node(t, parent);
            this->size++;
            return parent->left;
        }

        Node* add_right(Node* parent, T t){
            if (parent->right) throw exception();
            parent->right = new Node(t, parent);
            this->size++;
            return parent->right;
        }

        Node* delete_node(Node* node){
            if (node->left || node->right) throw exception();
            if (node == this->root) {
                this->root = nullptr;
            } else {
                if (node == node->parent->left){
                    node->parent->left = nullptr;
                } else {
                    node->parent->right = nullptr;
                }
            }
            delete node;
            this->size--;
        }

        void traverse_preorder(Node* walk=this->root){
            
        }
};


int main() {
    Tree<int> T;
    T.set_root(0);
    cout << *(T.get_root()) << endl;
}