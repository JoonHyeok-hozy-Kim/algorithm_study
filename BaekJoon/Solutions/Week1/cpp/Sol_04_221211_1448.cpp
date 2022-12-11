/*
1448 삼각형 만들기
https://www.acmicpc.net/problem/1448
*/


#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <numeric>

int N;
int straws[1000000];
int visited[1000000] = {};


bool cmp(int a, int b){
    return a > b;
}


int main(){
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    std::cin >> N;
    for (int i=0; i<N; i++){
        std::cin >> straws[i];
    }

    std::sort(straws, straws+N, cmp);
    
    int result = -1;
    for (int j=0; j<N-2; j++){
        if (straws[j] >= straws[j+1] + straws[j+2]) continue;
        else {
            result = straws[j] + straws[j+1] + straws[j+2];
            break;
        }
    }
    
    std::cout << result << std::endl;
}