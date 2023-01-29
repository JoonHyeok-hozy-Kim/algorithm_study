#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> M;
    vector<int> result;
    
    for (int i=0; i<nums.size(); i++){
        if (M.find(target - nums[i]) == M.end()){
            M.insert({nums[i], i});
        } else {
            result.push_back(M.find(target - nums[i])->second);
            result.push_back(i);
            break;
        }
    }
    
    return result;
    
}