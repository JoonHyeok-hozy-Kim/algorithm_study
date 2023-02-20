#include <iostream>
#include <vector>
#include <deque>
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
};

template <typename T>
void print_deque(deque<T> D){
    cout << "{ ";
    for (auto k : D){
        cout << *k << " ";
    }
    cout << "}\n";
}

template <typename T>
void print_vector(vector<T> V){
    cout << "[ ";
    for (auto c : V){
        cout << c << " ";
    }
    cout << "]\n";
}

template <typename T>
void print_vector_vector(vector<T> V){
    cout << "< ";
    for (auto v : V){
        cout << "[ ";
        for (auto c : v){
            cout << c << " ";
        }
        cout << "] ";
    }
    cout << ">\n";
}

void recursive(vector<vector<int>> &res, vector<int> &bv, deque<TreeNode<int>*> &cand){
    if (cand.empty()){
        vector<int> new_vector = bv;
        res.push_back(new_vector);
    } else {
        // cout << "cand : ";
        // if (cand.empty()) cout << endl;
        // else print_deque(cand);
        // cout << "bv : ";
        // if (!bv.empty()) print_vector(bv);
        // else cout << endl;
        // cout << "res : ";
        // if (!res.empty()) print_vector_vector(res);
        // else cout << endl;
        // cout << endl;


        TreeNode<int> *curr = cand.front();
        bv.push_back(curr->data);
        cand.pop_front();
        int child_cnt = 0;
        if (curr->left) {
            cand.push_back(curr->left);
            child_cnt++;
        }
        if (curr->right) {
            cand.push_back(curr->right);
            child_cnt++;
        }

        int cand_cnt = cand.size();
        if (cand_cnt == 0) recursive(res, bv, cand);
        else {
            for (int i=0; i<cand_cnt; i++){
                // cout << "Before call, cand : ";
                // print_deque(cand);
                recursive(res, bv, cand);
                // cand.push_back(cand.front());
                // cand.pop_front();
            }
        }

        for (int i=0; i<child_cnt; i++) cand.pop_back();
        bv.pop_back();
        cand.push_back(curr);
    }
}

void print_array(TreeNode<int>* root){
    vector<vector<int>> result;
    vector<int> build_vector;
    deque<TreeNode<int>*> candidates;
    candidates.push_back(root);
    recursive(result, build_vector, candidates);

    for (auto v : result){
        cout << "{ ";
        for (auto c : v){
            cout << c << " ";
        }
        cout << "} ";
    }
}

int main(){
    TreeNode<int> *t0 = new TreeNode<int>(2);
    t0->left = new TreeNode<int>(1);
    t0->right = new TreeNode<int>(3);

    // cout << *t0 << endl;    
    // deque<TreeNode<int>*> D;
    // D.push_back(t0);
    // D.push_back(t0->left);
    // D.push_back(t0->right);
    // print_deque(D);

    // print_array(t0);

    TreeNode<int> *t1 = new TreeNode<int>(4);
    t1->left = new TreeNode<int>(2);
    t1->right = new TreeNode<int>(6);
    t1->left->left = new TreeNode<int>(1);
    t1->left->right = new TreeNode<int>(3);
    t1->right->left = new TreeNode<int>(5);
    t1->right->right = new TreeNode<int>(7);

    print_array(t1);
}