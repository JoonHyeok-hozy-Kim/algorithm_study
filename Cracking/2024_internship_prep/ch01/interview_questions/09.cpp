#include <iostream>
#include <algorithm>
using namespace std;

int rabin_karp_hash(string &S, int start, int end){
    int power = 1;
    int result = 0;
    
    while (start <= end){
        result += ((int) S[start]) * power;
        power *= 3;
        start++;
    }
    
    return result;
}


bool is_substring(string &T, string &P){
    if (T.size() < P.size()) return false;

    int t_hash = rabin_karp_hash(T, 0, T.size()-1);
    for (int i=0; i<T.size()-P.size()+1; i++){
        if (t_hash == rabin_karp_hash(P, 0, P.size()-1)){
            return true;
        }
    }    
    return false;
}


bool check_rotation(string &S1, string &S2){
    if (S1.size() != S2.size()) return false;
    
    sort(S1.begin(), S1.end());
    sort(S2.begin(), S2.end());
    
    return is_substring(S1, S2);
}


int main() {
    string s1 = "abcd";
    string s2 = "bdca";
    string s3 = "abce";

    cout << boolalpha << check_rotation(s1, s2) << endl;
    cout << boolalpha << check_rotation(s1, s3) << endl;
}
