#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;

bool check_palindrome(vector<char> &str){
    unordered_map<char, int> M;
    
    for (auto i=str.begin(); i!=str.end(); i++){
        auto found = M.find(*i);
        if (found == M.end()){
            M.insert({*i, 1});
        } else {
            found->second++;
        }
    }
    
    bool one_found = false;
    for (auto i=M.begin(); i != M.end(); i++){
        if (i->second == 1){
            if (one_found){
                return false;
            } else {
                one_found = true;
            }
        } else if (i->second % 2 != 0){
            return false;
        }
    }
    
    return true;
}

bool in_place_check_palindrome(vector<char> &str){
    sort(str.begin(), str.end());
    
    bool one_found = false;
    int repeat_cnt = 1;
    for (auto i=str.begin()+1; i!=str.end(); i++){
        if (*(i-1) == *i){
            repeat_cnt++;
        } else {
            if (repeat_cnt == 1){
                if (one_found){
                    return false;
                } else {
                    one_found = true;
                }
            } else if (repeat_cnt % 2 != 0){
                return false;
            }
            
            repeat_cnt = 1;
        }

        // cout << *(i-1) << " vs " << *i << ", rep_cnt : " << repeat_cnt << ", one_found : " << one_found << endl;
    }
    
    if ((repeat_cnt == 1 && one_found) || (repeat_cnt > 1 && repeat_cnt % 2 != 0)){
        return false;
    }
    return true;
}


int main() {
    vector<char> v1 = {'a','a','b'};
    vector<char> v2 = {'a','a','a'};
    vector<char> v3 = {'a','a','a', 'a','b'};
    vector<char> v4 = {'a','a','b', 'b'};
    vector<char> v5 = {'a','a','b', 'c'};

    cout << boolalpha << check_palindrome(v1) << endl;
    cout << boolalpha << check_palindrome(v2) << endl;
    cout << boolalpha << check_palindrome(v3) << endl;
    cout << boolalpha << check_palindrome(v4) << endl;
    cout << boolalpha << check_palindrome(v5) << endl;

    cout << boolalpha << in_place_check_palindrome(v1) << endl;
    cout << boolalpha << in_place_check_palindrome(v2) << endl;
    cout << boolalpha << in_place_check_palindrome(v3) << endl;
    cout << boolalpha << in_place_check_palindrome(v4) << endl;
    cout << boolalpha << in_place_check_palindrome(v5) << endl;
}