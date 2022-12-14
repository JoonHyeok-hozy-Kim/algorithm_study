#include <iostream>
#include <algorithm>
using namespace std;

int * points[100000];

bool compare(int * p1, int * p2){
    if (p1[1] < p2[1]) {
        return true;
    } else if (p1[1] > p2[1]) {
        return false;
    } else {
        return p1[0] < p2[0]; 
    }
}

int main() {
    int N;
    cin >> N;

    for (int i=0; i<N; i++){
        points[i] = (int *) malloc(2 * sizeof(int));
        cin >> points[i][0] >> points[i][1];
    }

    // for (int i=0; i<N; i++){
    //     cout << "(" << points[i][0] << ", " << points[i][1] << ")" << endl;
    // }

    sort(points, points+N, compare);

    for (int i=0; i<N; i++){
        cout << points[i][0] << " " << points[i][1] << '\n';
    }
}