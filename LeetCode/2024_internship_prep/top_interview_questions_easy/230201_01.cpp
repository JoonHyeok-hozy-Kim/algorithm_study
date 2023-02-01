#include <iostream>
using namespace std;

int powersOfTwo(int n){
    int result;
    if (n <= 0) return 0;
    else if (n == 1) result = 1;
    else {
        int prev = powersOfTwo(n / 2);
        result = 2 * prev;
    }
    return result;
}

int main(){
    for (int i=0; i<=32; i++){
        cout << i << " : " << powersOfTwo(i) << endl;
    }
}