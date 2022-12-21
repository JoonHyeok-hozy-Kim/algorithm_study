/*
반전 요세푸스
https://www.acmicpc.net/problem/20301
*/

#include <iostream>
#include <deque>
using namespace std;

typedef deque<int> di;

int operate(di * q, int k, int m, int cnt, bool reverse){
    // cout << "cnt : " << cnt << ", reverse : " << boolalpha << reverse << endl;/
    int temp;
    for (int i=0; i<k; i++){
        if (reverse){
            temp = q->back();
            q->pop_back();
            if (i==k-1){
                printf("%d\n", temp);
                cnt++;
            } else {
                q->push_front(temp);
            }  
        } else {
            temp = q->front();
            q->pop_front();
            if (i==k-1){
                printf("%d\n", temp);
                cnt++;
            } else {
                q->push_back(temp);
            }
        }          
    }
    return cnt;
}

int main(){
    int N, K, M;
    scanf("%d %d %d", &N, &K, &M);

    di Q;
    for (int i=0; i<N; i++){
        Q.push_back(i+1);
    }

    int deleted_cnt = 0;
    bool reverse_flag = false;
    while (Q.size()){
        deleted_cnt = operate(&Q, K, M, deleted_cnt, reverse_flag);      
        if (deleted_cnt % M == 0) {
            reverse_flag = !reverse_flag;
        }  
    }
}