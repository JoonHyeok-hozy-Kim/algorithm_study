/*
9935. 문자열 폭발
https://www.acmicpc.net/problem/9935
*/
#include <iostream>
#include <list>
using namespace std;
string given_str;
string explosive;
list<char> str_list;
list<size_t> check_points;

bool execute_explosion(){

}

bool find_match(){
    size_t sl_idx = 0;
    auto sl_itr = str_list.begin();
    auto cp_itr = check_points.begin();
    while (cp_itr != check_points.end()){
        while (sl_idx < *cp_itr) sl_idx++;
        auto c_sl_itr = sl_itr;
        for (size_t i=0; i<explosive.size(); i++){

        }
        cp_itr++;
    }
}

int main() {
    cin.sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> given_str;
    cin >> explosive;

    for(size_t i=0; i<given_str.size(); i++){
        str_list.push_back(given_str[i]);
        if (given_str[i] == explosive[0]) check_points.push_back(i);
    }

    while (true){

    }
}