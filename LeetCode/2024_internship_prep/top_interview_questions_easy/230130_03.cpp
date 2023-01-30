#include <iostream>
using namespace std;

bool isPalindrome(string s) {
    int i = 0;
    int j = s.size()-1;
    
    while (i <= j){
        if (!isalnum(s[i])) {
            i++;
        } else if (!isalnum(s[j])){
            j--;
        } else {
            if (s[i] == s[j] || 
                (s[i] >= 'A' && s[j] >= 'A' && (s[i]-'a' == s[j]-'A' || s[i]-'A' == s[j]-'a'))){
                i++;
                j--;
            } else {
                return false;
            }
        }
    }
    
    return true;
}