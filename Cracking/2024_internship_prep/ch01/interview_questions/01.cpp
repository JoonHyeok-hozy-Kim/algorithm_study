#include <vector>
#include <iostream>
#include <unordered_set>
#include <algorithm>
using namespace std;


bool fastest_sol_int(vector<int> &V){
    unordered_set<int> S;
    for (int a : V){
        if (S.find(a) == S.end()){
            S.insert(a);
        } else {
            return false;
        }
    }
    return true;
}

template <typename T>
bool fastest_sol(vector<T> &V){
    unordered_set<T> S;
    for (T a : V){
        if (S.find(a) == S.end()){
            S.insert(a);
        } else{
            return false;
        }
    }
    return true;
}

bool in_place_sol_int(vector<int> &V){
    sort(V.begin(), V.end());
    auto i = V.begin();
    auto j = V.begin();
    j++;
    while (j != V.end()){
        if (*i == *j) {
            return false;
        }
        else {
            i++;
            j++;
        }
    }
    return true;
}


template <typename T>
bool in_place_sol(vector<T> &V){
    sort(V.begin(), V.end());
    auto i = V.begin();
    auto j = V.begin();
    j++;
    while (j != V.end()){
        if (*i == *j) {
            return false;
        }
        else {
            i++;
            j++;
        }
    }
    return true;
}

int main() {
    vector<int> v1 = {1, 2, 3, 4, 5};
    vector<int> v2 = {1, 2, 3, 3, 5};
    vector<int> v3 = {'a', 'b', 'c', 'd'};
    vector<int> v4 = {'a', 'b', 'b', 'd'};

    cout << "<fastest_sol_int test>" << endl;
    cout << boolalpha << fastest_sol_int(v1) << endl;
    cout << boolalpha << fastest_sol_int(v2) << endl;

    cout << "<fastest_sol test>" << endl;
    cout << boolalpha << fastest_sol(v1) << endl;
    cout << boolalpha << fastest_sol(v2) << endl;
    cout << boolalpha << fastest_sol(v3) << endl;
    cout << boolalpha << fastest_sol(v4) << endl;

    cout << "<in_place_sol_int test>" << endl;
    cout << boolalpha << in_place_sol_int(v1) << endl;
    cout << boolalpha << in_place_sol_int(v2) << endl;

    cout << "<in_place_sol test>" << endl;
    cout << boolalpha << in_place_sol(v1) << endl;
    cout << boolalpha << in_place_sol(v2) << endl;
    cout << boolalpha << in_place_sol(v3) << endl;
    cout << boolalpha << in_place_sol(v4) << endl;
}