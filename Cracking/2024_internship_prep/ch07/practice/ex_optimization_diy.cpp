#include <iostream>
#include <unordered_map>
using namespace std;

// 5 2 XXXXX
void find_index(string& ls, string& ss);
bool same_map(unordered_map<char, int>& m1, unordered_map<char, int>& m2);

void find_index(string& ls, string& ss){
    char first_char, last_char;
    unordered_map<char, int> given_map, temp_map;
    int i=0;
    int last_start = ls.size() - ss.size() + 1;

    first_char = ls[0];
    for (int j=0; j<ss.size(); j++){
        auto found_given = given_map.find(ls[i+j]);
        if (found_given == given_map.end()){
            given_map.insert({ls[i+j], 1});
            temp_map.insert({ls[i+j], 1});
        } else {
            found_given->second++;
            temp_map.find(ls[i+j])->second++;
        }
    }

    if (same_map(given_map, temp_map)) cout << i << " ";

    while (i <= last_start){
        if (temp_map.find(first_char)->second == 1) temp_map.erase(first_char);
        else temp_map.find(first_char)->second--;
        i++;
        first_char = ls[i];
        auto found_temp = temp_map.find(first_char);
        if (found_temp == temp_map.end()) temp_map.insert({first_char, 1});
        else found_temp->second++;

        if (same_map(given_map, temp_map)) cout << i << " ";
    }
}

bool same_map(unordered_map<char, int>& m1, unordered_map<char, int>& m2){
    auto k = m1.begin();
    while (k != m1.end()){
        auto k_found = m2.find(k->first);
        if (k_found == m2.end()) return false;
        else if (k_found->second != m1.find(k->first)->second) return false;
        k++;
    }
    return true;
}

int main() {
    string ls = "cbabadcbbabbcbabaabccbabc";
    string ss = "abbc";

    find_index(ls, ss);
}