#include <iostream>
#include <vector>
using namespace std;

void urlify(vector<char> &V){
    auto i = V.end()-1;
    auto j = V.end()-1;
    bool j_hit = false;
    while (j != V.begin()-1){
        if (!j_hit && *j == ' '){
            j--;
        } else if (!j_hit && *j != ' '){
            j_hit = true;
            *i = *j;
            i--;
            j--;
        } else if (j_hit && *j != ' '){
            *i = *j;
            i--;
            j--;
        } else {
            while (j != V.begin()-1 && *j == ' ') j--;
            j_hit = false;
            *i = '0';
            i--;
            *i = '2';
            i--;
            *i = '%';
            i--;
        }
    }
}

int main() {
    string s1 = "Mr John Smith    ";
    vector<char> v1(s1.begin(), s1.end());
    for (char c : v1) cout << c;
    cout << endl;
    urlify(v1);
    for (char c : v1) cout << c;
    cout << endl;
}