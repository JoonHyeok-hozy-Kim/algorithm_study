#include <unordered_map>
using namespace std;

int firstUniqChar(string s) {
    unordered_map<char, int> M;;
    
    for (int i=0; i<s.size(); i++){
        if (M.find(s[i]) == M.end()){
            M.insert({s[i], 1});
        } else {
            M.find(s[i])->second++;
        }
    }
    
    for (int i=0; i<s.size(); i++){
        if (M.find(s[i])->second == 1){
            return i;
        }
    }
    
    return -1;
}