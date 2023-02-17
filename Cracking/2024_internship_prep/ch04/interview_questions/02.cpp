#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

template <typename T>
class Node{
    public:
        T data;
        Node *left = nullptr;
        Node *right = nullptr;

        Node(T t) : data(t) {};
};

template <typename T>
Node<T>* generate_recursively(vector<T>& vec, unordered_set<T>* included, int start, int end){
    // cout << "start : " << start << " / end : " << end << endl;
    T target = vec[(start + end)/2];
    if (included->find(target) != included->end()) return nullptr;

    Node<T>* new_node = new Node<T>(target);
    included->insert(target);
    
    new_node->left = generate_recursively(vec, included, start, (start+end)/2);
    new_node->right = generate_recursively(vec, included, (start+end)/2 + 1, end);

    cout << "node : " << new_node->data << " (left : ";
    if (new_node->left != nullptr) {
        cout << new_node->left->data;
    }
    cout << ", right : ";
    if (new_node->right != nullptr) {
        cout << new_node->right->data;
    }
    cout << ")" << endl;
    return new_node;
}


int main() {
    vector<int> v;
    for (int i=0; i<6; i++){
        v.push_back(i);
    }

    unordered_set<int> included;
    Node<int> *root = generate_recursively(v, &included, 0, v.size()-1);
    
}