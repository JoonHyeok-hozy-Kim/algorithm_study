#include <iostream>
using namespace std;

void reverse(char* str) {
    char* start = str;
    char* end = str;
    char temp;
    while (*(end+1) != '\0') end++;
    while (start != end && start != end+1){
        temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

void print(char* str){
    char* s = str;
    while (*(s) != '\0') {
        printf("%c", *s);
        s++;
    }
    printf("\n");
}

int main() {
    char* S = new char[5];
    for (int i=0; i<4; i++){
        S[i] = i+65;
    }
    S[4] = '\0';

    char* s1 = S;
    print(s1);

    char* s2 = S;
    reverse(s2);
    print(S);

    // char* c1 = new char;
    // *c1 = 'c';
    // char c2;
    // c2 = *c1;
    // printf("%c", c2);
}