#include <iostream>
#include <queue>
using namespace std;

class Node {
    public:
        int val;
        Node *n1 = nullptr;
        Node *n2 = nullptr;

        Node(int v) : val(v) {};
        ~Node() {
            delete n1;
            delete n2;
            cout << val << " deleted." << endl;
        };

        void preorder() {
            cout << val << "-";
            if (n1) {
                n1->preorder();
            }
            if (n2) {
                n2->preorder();
            }
        }

        void breadth_first() {
            queue<pair<Node*, int>> Q;
            Q.push({this, 0});
            while (!Q.empty()) {
                pair<Node*, int> popped = Q.front();
                Q.pop();
                cout << popped.first->val << " ";
                if (popped.first->n1) Q.push({popped.first->n1, popped.second+1});      
                if (popped.first->n2) Q.push({popped.first->n2, popped.second+1});                
                if (!Q.empty() && popped.second != Q.front().second){
                    cout << endl;
                }
            }
            cout << endl;
        }

        void generate_tree(int level) {
            queue<pair<Node*, int>> Q;
            Q.push({this, 0});
            int new_val = val * 10;
            while (!Q.empty()) {
                pair<Node*, int> popped = Q.front();
                Q.pop();

                if (popped.second >= level) continue;

                if (popped.first->n1 == nullptr) {
                    Node *nn1 = new Node(new_val++);
                    popped.first->n1 = nn1;                    
                }
                Q.push({popped.first->n1, popped.second+1});
                
                if (popped.first->n2 == nullptr) {
                    Node *nn2 = new Node(new_val++);
                    popped.first->n2 = nn2;                    
                }
                Q.push({popped.first->n2, popped.second+1});
            }
        }
};

void _recursive(Node* original, Node* node) {
    if (original->n1) {
        Node *nn1 = new Node(original->n1->val);
        node->n1 = nn1;
        _recursive(original->n1, node->n1);
    }

    if (original->n2) {
        Node *nn2 = new Node(original->n2->val);
        node->n2 = nn2;
        _recursive(original->n2, node->n2);
    }
};

Node* copyStructure(Node* original) {
    Node *new_node = new Node(original->val);
    _recursive(original, new_node);
    return new_node;
};


int main() {
    Node* root = new Node(1);
    root->generate_tree(4);
    root->breadth_first();

    cout << "\nCopy" << endl;
    Node* root_copy = copyStructure(root);

    root->n2 = nullptr;
    
    cout << "\nOriginal" << endl;
    root->breadth_first();
    
    cout << "\nCopy" << endl;
    root_copy->breadth_first();
};