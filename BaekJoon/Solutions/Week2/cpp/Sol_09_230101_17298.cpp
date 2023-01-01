/*
오큰수 
https://www.acmicpc.net/problem/17298
*/

#include <iostream>
#include <stack>
using namespace std;

int * arr;

int main() {
    int N;
    scanf("%d\n", &N);

    arr = new int[N];
    for (int i = 0; i<N; i++) scanf(" %d", &(arr[i]));
    // for (int i = 0; i<N; i++) printf(" %d", arr[i]);

    stack<int> okun;
    int new_i;
    for (int i=N-1; i>=0; i--){
        new_i = -1;
        
        while (! okun.empty()){
            if (okun.top() > arr[i]){
                new_i = okun.top();
                break;
            } else {
                okun.pop();
            }
        }

        okun.push(arr[i]);
        arr[i] = new_i;
    }

    for (int i = 0; i<N; i++) printf("%d ", arr[i]);

}