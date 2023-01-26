#include <vector>
#include <unordered_set>
using namespace std;

bool containsDuplicate(vector<int>& nums) {
    unordered_set<int> S;
    
    for (int i=0; i<nums.size(); i++){
        if (S.find(nums[i]) != S.end()){
            return true;
        } else {
            S.insert(nums[i]);
        }
    }
    return false;
}