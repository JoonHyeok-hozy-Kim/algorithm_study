#include <iostream>
using namespace std;


int myAtoi(string s) {
    long long temp = 0;
    int int_max = (2<<29) - 1 + (2<<29);  // 2^31-1
    int int_min = -(2<<29) - (2<<29);     // -2^31
    int result;
    
    int i = 0;
    int sign = 1;
    while (i < s.size() && s[i] == ' ') i++;
    
    if (i != s.size()) {
        if (s[i] == '-'){
            sign = -1;
            i++;
        } else if (s[i] == '+'){
            i++;
        }
    }
    
    while (i < s.size() && isdigit(s[i])){
        temp *= 10;
        temp += s[i] - '0';
        i++;
        if (temp*sign >= int_max || temp*sign <= int_min) break;
    }
    
    temp *= sign;
    
    if (temp > int_max) {
        result = (int) int_max;
    } else if (temp < int_min){
        result = (int) int_min;
    } else {
        result = (int) temp;
    }
    
    return result;
}