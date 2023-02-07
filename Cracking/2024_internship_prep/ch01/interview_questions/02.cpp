#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

bool permutation_check(vector<string> &S1, vector<string> &S2){
    if (S1.size() != S2.size()) return false;
    
    unordered_map<string, int> US;
    for (int i=0; i<S1.size(); i++){
        auto found1 = US.find(S1[i]);
        if (found1 == US.end()){
            US.insert({S1[i], 1});
        } else {
            found1->second++;
        }
    }

    for (int i=0; i<S2.size(); i++){
        auto found2 = US.find(S2[i]);
        if (found2 == US.end() || found2->second == 0){
            return false;
        } else {
            found2->second--;
        }
    }
    return true;
}


int main() {
    vector<string> v1 = {"a", "b", "c"};
    vector<string> v2 = {"c", "b", "a"};
    vector<string> v3 = {"c", "b", "k"};
    vector<string> v4 = {"c", "b", "b"};
    vector<string> v5 = {"b", "c", "b"};

    cout << "v1 - v2 : " << boolalpha << permutation_check(v1, v2) << endl;
    cout << "v1 - v2 : " << boolalpha << permutation_check(v1, v3) << endl;
    cout << "v1 - v2 : " << boolalpha << permutation_check(v1, v4) << endl;
    cout << "v1 - v2 : " << boolalpha << permutation_check(v4, v5) << endl;
}