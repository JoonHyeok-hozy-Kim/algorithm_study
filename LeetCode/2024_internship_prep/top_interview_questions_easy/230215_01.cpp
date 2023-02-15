#include <vector>
#include <iostream>
#include <limits>
using namespace std;

string longest_common_prefix(vector<string> V){
    int i=0;
    vector<char> result;
    // int min_length = (1<<29) - 1 + (1<<29);
    int min_length = INT32_MAX;
    
    for (int j=0; j<V.size(); j++){
        min_length = (min_length < V[j].size()) ? min_length : V[j].size();
    }
    
    char target;
    bool common;
    for (int k=0; k<min_length; k++){
        target = V[0][k];
        common = true;
        for (int l=1; l<V.size(); l++){
            if (V[l][k] != target){
                common = false;
                break;
            }
        }
        if (common) {
            result.push_back(target);
        } else {
            break;
        }
    }
    
    if (result.size() == 0){
        return "";
    } else {
        return string(result.begin(), result.end());
    }    
}


int main() {
    vector<string> v1 = {"flower","flow","flight"};
    cout << "RESULT : " << longest_common_prefix(v1) << endl;

    vector<string> v2 = {"dog","racecar","car"};
    cout << "RESULT : " << longest_common_prefix(v2) << endl;
}