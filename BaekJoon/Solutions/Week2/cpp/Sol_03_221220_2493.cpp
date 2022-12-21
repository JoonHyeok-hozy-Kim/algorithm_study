/*
탑
https://www.acmicpc.net/problem/2493
*/

#include <iostream>
#include <stack>
using namespace std;

int * towers;
int * results;

int main() {
    int N;
    scanf("%d", &N);

    if (N==1) {
        printf("0\n");
        return 0;
    }

    towers = (int*) malloc(N * sizeof(int));
    for (int i=0; i<N; i++){
        scanf(" %d", &towers[i]);
    }
    // for (int i=0; i<N; i++) printf("%d ", towers[i]);

    results = (int*) malloc(N * sizeof(int));
    results[0] = 0;

    stack<pair<int, int>> prev_highs;
    prev_highs.push({towers[0], 1});

    for (int i=1; i<N; i++){
        // printf("prev_highs' top : (%d, %d)\n", prev_highs.top().first, prev_highs.top().second);
        if (towers[i-1] >= towers[i]){
            results[i] = i;            
        } else {
            while (prev_highs.size() > 0 && prev_highs.top().first < towers[i]){
                prev_highs.pop();
            }

            if (prev_highs.size() == 0){
                results[i] = 0;
            } else {
                results[i] = prev_highs.top().second;
            }
        }
        prev_highs.push({towers[i], i+1});
    }

    for (int i=0; i<N; i++) printf("%d ", results[i]);
}