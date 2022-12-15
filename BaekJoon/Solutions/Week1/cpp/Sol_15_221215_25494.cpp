#include <iostream>
#include <algorithm>
using namespace std;

int solution(int a, int b, int c){
    int result = 0;
    for (int x=1; x<=a; x++){
        for (int y=1; y<=b; y++){
            for (int z=1; z<=c; z++){
                if (x % y == y % z && y % z == z % x){
                    result++;
                }
            }
        }
    }
    return result;
}

int main() {
    int T;
    int a, b, c;
    cin >> T;
    for (int i=0; i<T; i++){
        cin >> a >> b >> c;
        printf("%d\n", solution(a, b, c));
    }
}