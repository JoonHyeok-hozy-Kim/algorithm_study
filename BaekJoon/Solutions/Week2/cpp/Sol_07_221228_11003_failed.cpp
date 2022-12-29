/*
최솟값 찾기
https://www.acmicpc.net/problem/11003
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

// int * nums;
int nums[5000000];
priority_queue<int, vector<int>, greater<int>> Q;
unordered_map<int, int> popped;

int main() {
    int N, L;
    scanf("%d %d", &N, &L);

    // nums = (int *) malloc(N * sizeof(int));
    for (int i=0; i<N; i++){
        scanf(" %d", &(nums[i])); 
    }
    // for (int i=0; i<N; i++) printf(" %d", nums[i]); 

    for (int i=0; i<N; i++){
        if (i-L-1 >= 0){
            if (popped.find(nums[i-L-1]) != popped.end()){
                popped[nums[i-L-1]]++;
            } else {
                popped.insert({nums[i-L-1], 1});
            }
        }
        
        while (Q.size() > 0 && popped.size() > 0){
            if (popped.find(Q.top()) != popped.end()){
                if (popped[Q.top()] > 0){
                    popped[Q.top()]--;
                    Q.pop();
                    continue;
                } 
                // else {
                //     popped.erase(Q.top());
                // }
            }

            break;        
        }

        Q.push(nums[i]);

        printf("%d ", Q.top());
    }
    printf("\n");
}