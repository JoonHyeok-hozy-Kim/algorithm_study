#include <unordered_map>
using namespace std;

bool isAnagram(string s, string t) {
    unordered_map<char, int> M;
    
    for (char c : s){
        if (M.find(c) == M.end()){
            M.insert({c, 1});
        } else {
            M.find(c)->second++;
        }
    }
    
    for (char c : t){
        if (M.find(c) == M.end()){
            return false;
        } else if (M.find(c)->second == 1){
            M.erase(c);
        } else {
            M.find(c)->second--;
        }
    }
    
    if (M.size() == 0){
        return true;
    } else {
        return false;
    }
}