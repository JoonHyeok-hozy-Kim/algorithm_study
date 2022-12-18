/*
선 긋기
https://www.acmicpc.net/problem/2170
*/

#include <iostream>
#include <algorithm>
using namespace std;

int N;
int ** points;

int compare(int * p1, int * p2){
    return p1[0] < p2[0];
}

int main() {
    cin >> N;
    points = (int **) malloc(N * sizeof(int *));
    for (int i=0; i<N; i++) {
        points[i] = (int *) malloc(2 * sizeof(int));
        int x, y;
        scanf("%d %d", &x, &y);
        if (x > y) {
            points[i][0] = y;
            points[i][1] = x;
        } else {
            points[i][0] = x;
            points[i][1] = y;
        }
    }
    // for (int i=0; i<N; i++){
    //     cout << "( " << points[i][0] << ", " << points[i][1] << ") ";
    // }

    sort(points, points+N, compare);
    // for (int i=0; i<N; i++){
    //     cout << "(" << points[i][0] << ", " << points[i][1] << ") ";
    // }

    int result = 0;
    int start = points[0][0];
    int end = points[0][1];

    for (int i=1; i<N; i++){
        if (points[i][0] <= end){
            end = max(end, points[i][1]);
        } else {
            result += (end - start);
            start = points[i][0];
            end = points[i][1];
        }
    }

    result += (end - start);
    printf("%d", result);

}