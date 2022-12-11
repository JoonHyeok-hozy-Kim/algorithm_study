/*
1476. 날짜 계산
https://www.acmicpc.net/problem/1476
*/
#include <iostream>
using namespace std;


int main() {
    int E, S, M;
    cin >> E >> S >> M;

    int result = S-1;
    while (true){
        if (result % 15 == E-1 && result % 19 == M-1) break;
        else result += 28;
    }

    cout << result +1 << endl;
}