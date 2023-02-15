#include <unordered_map>
#include <iostream>
using namespace std;


int brute_force(string T, string P){
    if (P.size() == 0) return 0;

    if (T.size() >= P.size()){
        for (int i=0; i<T.size()-P.size()+1; i++){
            for (int j=0; j<=P.size(); j++){
                if (j == P.size()) return i;
                if (P[j] != T[i+j]) break;
            }
        }
    }

    return -1;
}

int rabin_karp(string &T, string &P){
    int t_hash = 0, p_hash = 0, base = 1;
    int cnt = 0;
    bool identical;
    for (int i=0; i<P.size(); i++){
        t_hash += ((int) T[i]) * base;
        p_hash += ((int) P[i]) * base;
        base *= 2;
    }
    base /= 2;
    
    while (cnt < T.size() - P.size() + 1) {
        // cout << t_hash << " / " << p_hash << endl;
        if (t_hash == p_hash){
            identical = true;
            for (int j=0; j<P.size(); j++){
                if (T[cnt+j] != P[j]){
                    identical = false;
                    break;
                }
            }
            if (identical) return cnt;
        }

        if (cnt == T.size() - P.size()) break;

        t_hash -= (int) T[cnt];
        t_hash /= 2;
        t_hash += ((int) T[cnt + P.size()]) * base;
        cnt++;
    }

    return -1;
}


int main(){
    string s1 = "awyawyawyxz";
    string s2 = "wyxz";

    cout << brute_force(s1, s2) << endl;
    cout << rabin_karp(s1, s2) << endl;
}