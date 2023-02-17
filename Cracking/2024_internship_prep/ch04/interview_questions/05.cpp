#include <iostream>
using namespace std;

template <typename T>
class TreeNode{
    public:
        T data;
        TreeNode* left = nullptr;
        TreeNode* right = nullptr;

        TreeNode(T t) : data(t) {};
        ~TreeNode() {
            if (this->left) delete left;
            if (this->right) delete right;
            cout << this->data << " deleted." << endl;
        }

        struct MinMax{
            T min_val;
            T max_val;
            bool result;
        };

        MinMax _validate_bst(){
            MinMax mm;
            if (this->left){
                MinMax mm1 = this->left->_validate_bst();
                if (!mm1.result) return mm1;
                else if (mm1.max_val > this->data){
                    mm.result = false;
                    return mm;
                } else {
                    mm.min_val = mm1.min_val;
                }
            } else {
                mm.min_val = this->data;
            }
            
            if (this->right){
                MinMax mm2 = this->right->_validate_bst();
                if (!mm2.result) return mm2;
                else if (mm2.min_val < this->data){
                    mm.result = false;
                    return mm;
                } else {
                    mm.max_val = mm2.max_val;
                }
            } else {
                mm.max_val = this->data;
            }

            if (mm.min_val <= this->data && mm.max_val >= this->data){
                mm.result = true;
            } else {
                mm.result = false;
            }

            return mm;
        }

        bool validate_bst(){
            return this->_validate_bst().result;
        }
};


int main(){
    TreeNode<int>* t1 = new TreeNode<int>(5);
    cout << boolalpha << t1->validate_bst() << endl;

    t1->left = new TreeNode<int>(3);
    cout << boolalpha << t1->validate_bst() << endl;

    t1->left->right = new TreeNode<int>(4);
    cout << boolalpha << t1->validate_bst() << endl;

    t1->right = new TreeNode<int>(10);
    cout << boolalpha << t1->validate_bst() << endl;

    t1->right->left = new TreeNode<int>(7);
    cout << boolalpha << t1->validate_bst() << endl;

    delete t1;
}