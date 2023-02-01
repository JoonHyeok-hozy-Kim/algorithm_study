#include <unordered_map>
#include <iostream>
using namespace std;


int boyer_moore(string T, string P){
    int n = T.size();
    int m = P.size();
    int i, j, k;
    unordered_map<char, int> last;

    if (m == 0) return 0;
    for (int x=0; x<m; x++){
        auto found = last.find(P[x]);
        if (found == last.end()){
            last.insert({P[x], x});
        } else {
            found->second = x;
        }
    }

    i = m - 1;
    k = m - 1;

    while (i < n){
        if (T[i] == P[i]){
            if (k == 0){
                return i;
            }

            i--;
            k--;
        } else {
            auto found2 = last.find(T[i]);
            
            if (found2 == last.end()){
                j = -1;
            } else {
                j = found2->second;
            }

            if (k < j+1){
                i += m - k;
            } else {
                i += m - (j+1);
            }

            k = m - 1;
        }
    }

    return -1;
}


int main(){
    string s1 = "aaaaaaaaazzwyxzaaaaa";
    string s2 = "wyxz";
    cout << boyer_moore(s1, s2) << endl;
}