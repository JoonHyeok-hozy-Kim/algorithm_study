#include <vector>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int i=0;
    int j;
    
    while (i < nums.size()-1){
        if (nums[i] == 0) {
            j = i+1;
            while (j < nums.size()){
                if (nums[j] == 0) {
                    j++;
                } else {
                    break;
                }
            }
            
            if (j == nums.size()){
                return;
            } else {
                nums[i] = nums[j];
                nums[j] = 0;
            } 
        }
        
        i++;
    }
}