/*
2866. 문자열 잘라내기
https://www.acmicpc.net/problem/2866
*/
#include <iostream>
#include <vector>
#include <set>
using namespace std;

class CharNode{
    public:
        char key;
        vector<CharNode*> children;

        CharNode(int c) { key = c; };
        ~CharNode() {
            if (children.size()){
                for (auto i=children.begin(); i!=children.end(); i++) delete (*i);
            }
        }

        CharNode * is_child(char c){
            for (auto i=children.begin(); i!=children.end(); i++){
                if ((*i)->key == c) return *i;
            }
            return nullptr;
        }

        CharNode * add_child(char c){
            CharNode * new_node = new CharNode(c);
            children.push_back(new_node);
            return new_node;
        }
};

int recursive_sol(CharNode * _char_node, vector<string> * _str_vec, int col, int row, int curr_cnt){
    if (row < 0) return curr_cnt;

    char target_char = (*_str_vec)[row][col];
    CharNode * next_node = (*_char_node).is_child(target_char);
    if (next_node == NULL) {
        next_node = (*_char_node).add_child(target_char);
        return recursive_sol(next_node, _str_vec, col, row-1, curr_cnt);
    } else {
        return recursive_sol(next_node, _str_vec, col, row-1, curr_cnt+1);
    }
}

int main() {
    static int R, C;
    cin >> R >> C;

    vector<string> str_vec;
    str_vec.reserve(R);
    for (int i=0; i<R; i++){
        string new_row;
        cin >> new_row;
        str_vec.push_back(new_row);
    }
    // for (string x : str_vec) cout << x << " ";

    CharNode root(' ');
    // CharNode * child = root.add_child('a');
    // cout << child->key << endl;
    // CharNode * is_it1 = root.is_child('a');
    // if (is_it1 == NULL) {
    //     cout << "Not Includes " << endl;
    // } else {
    //     cout << "Includes " << is_it1->key << endl;
    // }
    // CharNode * is_it2 = root.is_child('b');
    // if (is_it2 == NULL) {
    //     cout << "Not Includes " << endl;
    // } else {
    //     cout << "Includes " << is_it2->key << endl;
    // }

    int result_cnt = 0;
    for (int c=0; c<C; c++){
        int temp = recursive_sol(&root, &str_vec, c, R-1, 0);
        result_cnt = max(result_cnt, temp);
    }

    cout << R - 1 - result_cnt << endl;
}