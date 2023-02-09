#include <vector>
#include <iostream>
#include <sstream>
using namespace std;

string compress(string &str){
    int advantage = 0;
    int repeat_cnt = 1;
    vector<char> VC;
    vector<int> VI;
    
    for (auto i=str.begin()+1; i!=str.end(); i++){
        if (*(i-1) == *i) {
            repeat_cnt++;
        } else {
            advantage += repeat_cnt - 2;
            VC.push_back(*(i-1));
            VI.push_back(repeat_cnt);
            repeat_cnt = 1;
        }
    }

    advantage += repeat_cnt - 2;
    VC.push_back(*(str.end()-1));
    VI.push_back(repeat_cnt);
    
    if (advantage <= 0) return str;
    else {
        string result;
        stringstream ss;
        for (int i=0; i<VC.size(); i++){
            ss << VC[i];
            ss << VI[i];
        }
        ss >> result;
        return result;
    }
}


int main() {

    string s1 = "aabcccccaaa";
    cout << compress(s1) << endl;

    string s2 = "abbccc";
    cout << compress(s2) << endl;
}