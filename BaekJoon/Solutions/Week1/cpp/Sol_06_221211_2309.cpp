/*
2309. 일곱 난쟁이
https://www.acmicpc.net/problem/2309
*/
#include <iostream>
#include <algorithm>
using namespace std;


bool cmp(int a, int b) {
    return a < b;
}


int main() {
    int dwarves[9];
    int height_sum = 0;
    for (int i=0; i<9; i++){
        cin >> dwarves[i];
        height_sum += dwarves[i];
    }

    sort(dwarves, dwarves+9, cmp);

    int other_one;
    int other_two = -1;
    for (int i=0; i<9; i++){
        other_one = dwarves[i];
        for (int j=0; j<9; j++){
            if (other_one + dwarves[j] == height_sum - 100){
                other_two = dwarves[j];
                break;
            }
        }
        if (other_two > 0) break;
    }
    
    for (int d : dwarves){
        if (other_one > 0 && other_one == d){
            other_one = -1;
            continue;
        }
        else if (other_two > 0 && other_two == d){
            other_one = -1;
            continue;
        }
        cout << d << endl;
    }
}