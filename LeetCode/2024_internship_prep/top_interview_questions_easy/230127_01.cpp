#include <vector>
#include <unordered_set>
using namespace std;

int singleNumber(vector<int>& nums) {
    unordered_set<int> S;
    
    for (int n : nums){
        if (S.find(n) != S.end()){
            S.erase(n);
        } else {
            S.insert(n);
        }
    }
    
    return *S.begin();
}