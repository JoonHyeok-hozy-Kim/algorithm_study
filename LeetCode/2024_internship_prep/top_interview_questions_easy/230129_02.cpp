#include <iostream>
#include <queue>
using namespace std;

int reverse(int x) {
    queue<int> Q;
    while (x != 0){
        Q.push(x % 10);
        x /= 10;
    }
    
    int result = 0;
    int max_int = (2<<29) - 1 + (2<<29);
    int min_int = -(2<<29) - (2<<29);
    while (Q.size()){
        if (result > max_int/10 || result < min_int/10){
            result = 0;
            break;
        }
        
        result *= 10;
        result += Q.front();
        Q.pop();
    }
    
    return result;
}

int reverse(int x) {
    long long r = 0;
    while (x){
        r *= 10;
        r += x%10;
        x /= 10;
    }

    int int_max = (2<<29) - 1 + (2<<29);
    int int_min = -(2<<29) - (2<<29);
    if (r > int_max || r < int_min) return 0;
    return r;
}