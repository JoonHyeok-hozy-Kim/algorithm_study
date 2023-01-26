#include <vector>
#include <stack>
#include <queue>
#include <iostream>
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


int main() {
    vector<int> v1;
    v1.reserve(5);
    for (int i=0; i<5; i++) v1.push_back(i);
    for (int i=0; i<5; i++) {
        printf("%d ", v1.back());
        v1.pop_back();
    }
}