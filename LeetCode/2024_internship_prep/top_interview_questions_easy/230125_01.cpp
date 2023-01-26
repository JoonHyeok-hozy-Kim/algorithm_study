#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    
    int initial_size = nums.size();
    int temp;
    for (int i=0; i<initial_size; i++){
        if (nums.front()==nums.back() && nums.size() > 1){
            nums.erase(nums.begin());
        } else {
            temp = nums.front();
            nums.erase(nums.begin());
            nums.push_back(temp);
        }
    }
    return (int) nums.size();
}

void print_vector(vector<int>& nums){
    for (auto i=nums.begin(); i!=nums.end(); i++){
        printf("%d ", *i);
    }
    printf("\n");
}

int removeDuplicates2(vector<int>& nums) {
    int p = 0;
    int s = nums.size();
    for (int i=1; i<s; i++){
        if (nums[p] < nums[i]){
            nums[p+1] = nums[i];
            p++;
        }
    }
    return p+1;
}

int main(){
    vector<int> v1 = {1,2};
    print_vector(v1);
    removeDuplicates(v1);
    print_vector(v1);
    
    vector<int> v2 = {1,2,2,2,3,4,4,5};
    print_vector(v2);
    removeDuplicates2(v2);
    print_vector(v2);

}