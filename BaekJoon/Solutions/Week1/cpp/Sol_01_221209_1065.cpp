// 1065. 한수
// https://www.acmicpc.net/problem/1065

#include <iostream>


int main() {
    int N, result;
    std::cin >> N;

    if (N < 100){
        result = N;
    } else {
        result = 99;

        int temp = 100;
        while (temp <= N){
            if (temp == 1000) break;

            int a, b, c;
            a = temp / 100;
            b = (temp / 10) % 10;
            c = temp % 10;
            if (a - b == b - c) result += 1;
            temp += 1;
        }
    }

    std::cout << result;

    return 0;
}