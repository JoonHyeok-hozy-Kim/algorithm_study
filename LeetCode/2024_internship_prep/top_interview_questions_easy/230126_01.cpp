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

int main(){
    vector<int> v1 = {1,2};
    print_vector(v1);
    removeDuplicates(v1);
    print_vector(v1);

}