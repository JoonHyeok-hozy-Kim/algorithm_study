#include <vector>
#include <unordered_set>
#include <iostream>
using namespace std;

bool hash_sol(vector<char> &S1, vector<char> &S2){
    unordered_set<char> US;
    
    if (S1.size() == S2.size()-1){
        // INSERT CASE
        for (auto i=S2.begin(); i!=S2.end(); i++){
            US.insert(*i);
        }
        
        for (auto i=S1.begin(); i!=S1.end(); i++){
            if (US.find(*i)!= US.end()){
                US.erase(*i);
            }
        }
        
        if (US.size() == 1) return true;
    
    
    } else if (S1.size() == S2.size()+1){
        // REMOVE CASE
        for (auto i=S1.begin(); i!=S1.end(); i++){
            US.insert(*i);
        }
        
        for (auto i=S2.begin(); i!=S2.end(); i++){
            if (US.find(*i) != US.end()){
                US.erase(*i);
            }        
        }
        
        if (US.size() == 1) return true;    
    
    
    } else if (S1.size() == S2.size()){
        // REPLACE CASE, ZEOR EDITS CASE
        bool not_common_exist = false;
        
        for (auto i=S1.begin(); i!=S1.end(); i++){
            US.insert(*i);
        }
        
        for (auto i=S2.begin(); i!=S2.end(); i++){
            if (US.find(*i) != US.end()){
                US.erase(*i);
            } else {
                if (not_common_exist){
                    return false;
                } else {
                    not_common_exist = true;
                }
            }
        }
    
        return true;
    } 

    return false;
}


int main() {
    vector<char> v11 = {'p', 'a', 'l', 'e'};
    vector<char> v12 = {'p', 'l', 'e'};
    cout << boolalpha << hash_sol(v11, v12) << endl;
    
    vector<char> v21 = {'p', 'a', 'l', 'e', 's'};
    vector<char> v22 = {'p', 'a', 'l', 'e'};
    cout << boolalpha << hash_sol(v21, v22) << endl;
    
    vector<char> v31 = {'p', 'a', 'l', 'e'};
    vector<char> v32 = {'b', 'a', 'l', 'e'};
    cout << boolalpha << hash_sol(v31, v32) << endl;
    
    vector<char> v41 = {'p', 'a', 'l', 'e'};
    vector<char> v42 = {'b', 'a', 'k', 'e'};
    cout << boolalpha << hash_sol(v41, v42) << endl;
}