#include <iostream>
using namespace std;

int sum(int a, int b=5){
    return a + b;
}


int main() {
    cout << sum(10) << endl;
}