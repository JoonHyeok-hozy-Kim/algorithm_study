#include <iostream>
#include <vector>
using namespace std;

int main(){
    string s = "abcdef";
    vector<char> projects(s.begin(), s.end());
    vector<pair<char, char>> dependencies = {
        {'a', 'd'}, {'f', 'b'},  {'b', 'd'}, {'f', 'a'}, {'d', 'c'}
    };

    
}