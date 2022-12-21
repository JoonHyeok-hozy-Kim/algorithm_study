/*
감시 카메라
https://www.acmicpc.net/problem/5884
*/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
int ** herd;

void debug_vector(vector<pair<int, int>> l){
    for (int i=0; i<l.size(); i++){
        cout << "(" << l[i].first << ", " << l[i].second << ") ";
    }
    cout << endl;
}

int dfs(int cow_idx, vector<pair<int, int>> l){
    // debug_vector(l);

    if (l.size() > 3) {
        // cout << "Failed." << endl;
        return 0;
    }

    if (cow_idx == N){
        // cout << "Success!" << endl;
        return 1;
    }

    int temp_result;
    if (cow_idx == 0) {        
        l.push_back({herd[0][0], -1});
        temp_result = dfs(cow_idx+1, l);
        if (temp_result == 1) return 1;

        l.pop_back();
        l.push_back({-1, herd[0][1]});
        temp_result = dfs(cow_idx+1, l);
        if (temp_result == 1) return 1;

    } else {
        for (int i=0; i<l.size(); i++){
            if (l[i].first == herd[cow_idx][0] || l[i].second == herd[cow_idx][1]){
                temp_result = dfs(cow_idx+1, l);
                if (temp_result == 1) return 1;

            } else{
                l.push_back({herd[cow_idx][0], -1});
                temp_result = dfs(cow_idx+1, l);
                if (temp_result == 1) return 1;

                l.pop_back();
                l.push_back({-1, herd[cow_idx][1]});
                temp_result = dfs(cow_idx+1, l);
                if (temp_result == 1) return 1;
                l.pop_back();
            }
        }
    }

    return 0;
}

int main() {
    scanf("%d", &N);
    herd = (int **) malloc(N * sizeof(int *));
    for (int i=0; i<N; i++){
        herd[i] = (int *) malloc(2 * sizeof(int));
        scanf("%d %d", &(herd[i][0]), &(herd[i][1]));
    }

    if (N <= 3){
        printf("1\n");
    } else {    
        vector<pair<int, int>> l;
        printf("%d\n", dfs(0, l));
    }
}