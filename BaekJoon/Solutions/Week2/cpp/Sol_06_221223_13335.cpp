/*
트럭 
https://www.acmicpc.net/problem/13335
*/

#include <iostream>
#include <queue>
using namespace std;

queue<int> trucks;
queue<int> bridge;

int main() {
    int n, w, L;
    scanf("%d %d %d", &n, &w, &L);

    int temp;
    for (int i=0; i<n; i++){
        scanf(" %d", &temp);
        trucks.push(temp);
    }

    for (int i=0; i<w; i++) bridge.push(0);
    
    int time = 0;
    while (bridge.size() > 0){
        time++;
        L += bridge.front();
        bridge.pop();    

        if (trucks.size() > 0) {
            if (L >= trucks.front()){
                L -= trucks.front();
                bridge.push(trucks.front());
                trucks.pop();
            } else {
                bridge.push(0);
            }
        }    
    }

    printf("%d\n", time);
}