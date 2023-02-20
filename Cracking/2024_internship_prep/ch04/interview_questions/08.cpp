#include <iostream>
#include <vector>
using namespace std;

template <typename T>
class TreeNode{
    public:
        T data;
        TreeNode *parent = nullptr;
        TreeNode *left = nullptr;
        TreeNode *right = nullptr;

        TreeNode(T t) : data(t) {};
        TreeNode(T t, TreeNode* p) : data(t), parent(p) {};
        TreeNode(T t, TreeNode* l, TreeNode* r) : data(t), left(l), right(r) {};
        ~TreeNode(){
            if (this->left) delete this->left;
            if (this->right) delete this->right;
        }

        void get_depths(vector<int> *V, TreeNode* N1, TreeNode* N2, int depth=0){
            if (this == N1) (*V)[0] = depth;
            if (this == N2) (*V)[1] = depth;
            if (this->left) this->left->get_depths(V, N1, N2, depth+1);
            if (this->left) this->right->get_depths(V, N1, N2, depth+1);
        }
};

template <typename T>
TreeNode<T>* first_common_ancestor(TreeNode<T>* root, TreeNode<T>* N1, TreeNode<T>* N2){
    vector<int> depths = {0, 0};
    root->get_depths(&depths, N1, N2);
    cout << "depths : " << depths[0] << ", " << depths[1] << endl;

    TreeNode<T> *T1 = N1;
    TreeNode<T> *T2 = N2;

    while (T1 != T2){
        if (depths[0] == depths[1]){
            T1 = T1->parent;
            T2 = T2->parent;
            depths[0]--;
            depths[1]--;
        } else if (depths[0] < depths[1]){
            T2 = T2->parent;
            depths[1]--;
        } else {
            T1 = T1->parent;
            depths[0]--;
        }
    }
    return T1;
}

int main(){
    TreeNode<int>* t0 = new TreeNode<int>(0);
    t0->left = new TreeNode<int>(1, t0);
    t0->right = new TreeNode<int>(2, t0);
    t0->left->left = new TreeNode<int>(3, t0->left);
    t0->left->right = new TreeNode<int>(4, t0->left);
    t0->right->left = new TreeNode<int>(5, t0->right);
    t0->right->right = new TreeNode<int>(6, t0->right);

    TreeNode<int> *t1 = t0->left->left;
    TreeNode<int> *t2 = t0->left->right;
    TreeNode<int> *t3 = t0->right->right;

    cout << "Result : " << first_common_ancestor(t0, t1, t2)->data << endl;
    cout << "Result : " << first_common_ancestor(t0, t1, t3)->data << endl;
}