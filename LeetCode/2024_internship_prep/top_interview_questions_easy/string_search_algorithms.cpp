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

int _rk_hash(string& T, int index, int length){
    int result = 0;
    int power = 1;
    for (int i=0; i<length; i++){
        result += ((int) T[index+i]) * power;
        power *= 3; 
    }
    return result;
}

int rabin_karp(string T, string P){
    if (P.size() == 0) return 0;

    int p_hash = _rk_hash(P, 0, (int) P.size());

    for (int i=0; i<T.size()-P.size()+1; i++){
        if (p_hash == _rk_hash(T, i, P.size())) return i;
    }

    return -1;
}


int main(){
    string s1 = "awyawyxz";
    string s2 = "wyxz";

    cout << brute_force(s1, s2) << endl;
    cout << rabin_karp(s1, s2) << endl;
}