#include <iostream>
#include <vector>
#include <unordered_map>
#include <exception>
#include <algorithm>
using namespace std;

template <typename T>
void print(vector<T> V){
    cout << "[ ";
    for (auto c : V){
        cout << c << " ";
    }
    cout << "]\n";
}

vector<char> build_order(vector<char> &pj, vector<pair<char, char>> &dp){
    unordered_map<char, vector<char>> M;
    for (char c : pj){
        M.insert({c, {}});
    }

    for (auto d : dp){
        if (M.find(d.first) != M.end()){
            (M.find(d.first)->second).push_back(d.second);
        }
    }
}

int main(){
    string s = "abcdef";
    vector<char> projects(s.begin(), s.end());
    print(projects);
    vector<pair<char, char>> dependencies = {
        {'a', 'd'}, {'f', 'b'},  {'b', 'd'}, {'f', 'a'}, {'d', 'c'}
    };

    // vector<char> result = build_order(projects, dependencies);

    auto found = find(projects.begin(), projects.end(), 'c');
    cout << *(found) << endl;
}