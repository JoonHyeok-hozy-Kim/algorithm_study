/*
최솟값 찾기
https://www.acmicpc.net/problem/11003
*/

#include <cstdio>
#include <cstdlib>
#include <deque>
using namespace std;

// int * nums;
int nums[5000000];
deque<pair<int, int>> Q;

int main() {
    int N, L;
    scanf("%d %d", &N, &L);

    for (int i=0; i<N; i++){
        scanf(" %d", &(nums[i])); 
    }
    // for (int i=0; i<N; i++) printf(" %d %d\n", num_set[i][0], num_set[i][1]); 

    for (int i=0; i<N; i++){
        while (! Q.empty() && Q.front().first <= i-L){
            // printf("POP PAST i : %d, L : %d, target : %d\n", i, L, Q.front()[0]);
            Q.pop_front();
        }

        if (Q.empty()){
            Q.push_front({i, nums[i]});
        } else if (Q.front().second >= nums[i]){
            Q.clear();
            Q.push_front({i, nums[i]});
        } else {
            while (Q.back().second >= nums[i]){
                Q.pop_back();
            }
            Q.push_back({i, nums[i]});
        }

        // printf("Q : [");
        // if (Q.size() >= 1){
        //     printf("(%d, %d)", Q.front()[0], Q.front()[1]);
        // }
        // if (Q.size() == 2){
        //     printf("(%d, %d)", Q.back()[0], Q.back()[1]);
        // }
        // printf("]\n");
        printf("%d ", Q.front().second);
    }

}