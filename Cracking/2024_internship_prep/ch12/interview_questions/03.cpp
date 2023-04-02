#include <iostream>
#include <unordered_map>
#include <map>
using namespace std;

int main() {
    map<int, int> m1;
    unordered_map<int, int> u1;

    for (int i=0; i<10; i++){
        m1.insert({i, i*100});
        u1.insert({i, i*100});
    }
    
    cout << "Map" << endl;
    for (const auto& kv: m1){
        cout << kv.first << " / " << kv.second << endl;
    }
    
    cout << "Unordered Map" << endl;
    for (const auto& kv: u1){
        cout << kv.first << " / " << kv.second << endl;
    }
}