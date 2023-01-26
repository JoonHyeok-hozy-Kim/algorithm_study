#include <vector>
#include <stack>
#include <queue>
using namespace std;

void rotate(vector<int>& nums, int k) {
    stack<int> S;
    queue<int> Q;
    k %= nums.size();
    
    if (k==0) return;
    
    for (int i=0; i<k; i++){
        S.push(nums.back());
        nums.pop_back();
    }
    while (S.size()){
        Q.push(S.top());
        S.pop();
    }
    
    while (nums.size()){
        S.push(nums.back());
        nums.pop_back();
    }
    while (S.size()){
        Q.push(S.top());
        S.pop();
    }
    
    while (Q.size()){
        nums.push_back(Q.front());
        Q.pop();
    }
}