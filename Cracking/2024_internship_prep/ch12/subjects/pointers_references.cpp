#include <iostream>
using namespace std;

void test1(){
    cout << "\n[Test 1 : pointer]" << endl;
    int *p = new int;
    *p = 7;
    int *q = p;
    *q = 9;
    cout << *p << endl;

}

void test2(){
    cout << "\n[Test 2 : reference]" << endl;
    int a = 5;
    int &b = a;     // Reference cannot be null!
    b = 3;
    cout << a << endl;
}

void test3(){
    cout << "\n[Test 3 : pointer arithmetic]" << endl;
    int *p = new int[2];
    p[0] = 1;
    p[1] = 2;
    cout << *p << endl;
    p++;
    cout << *p << endl;
}

int main() {
    test1();
    test2();
    test3();
}