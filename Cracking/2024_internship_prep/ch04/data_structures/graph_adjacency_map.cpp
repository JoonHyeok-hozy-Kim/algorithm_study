#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;

bool exists_root(unordered_map<int, vector<int>> *E, int from, int to){
    queue<int> Q;
    Q.push(from);
    int temp;
    unordered_set<int> visited;

    while (!Q.empty()){
        temp = Q.front();
        cout << temp << " ";
        Q.pop();
        if (temp == to){
            return true;
        } else {
            if (visited.find(temp) == visited.end() && E->find(temp) != E->end()){
                for (int c : E->find(temp)->second){
                    Q.push(c);
                }
            }
        }
        visited.insert(temp);
    }
    return false;
}

int main(){
    unordered_map<int, vector<int>> edge_map;
    unordered_set<int> vertex_set;

    edge_map.insert({1, {}});
    edge_map.find(1)->second.push_back(2);
    edge_map.find(1)->second.push_back(3);
    edge_map.find(1)->second.push_back(4);

    edge_map.insert({3, {}});
    edge_map.find(3)->second.push_back(5);
    edge_map.find(3)->second.push_back(6);

    edge_map.insert({4, {}});
    edge_map.find(4)->second.push_back(7);

    edge_map.insert({7, {}});
    edge_map.find(7)->second.push_back(8);

    cout << boolalpha << exists_root(&edge_map, 6, 8);

    edge_map.insert({6, {}});
    edge_map.find(6)->second.push_back(4);

    cout << boolalpha << exists_root(&edge_map, 6, 8);
}