#include <iostream>
#include <algorithm>
using namespace std;

int arr[100000];

int main() {
    int N;
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> arr[i];
    }
    sort(arr, arr+N);

    int prev = -1001;
    for (int i=0; i<N; i++) {
        if (arr[i] != prev){
            cout << arr[i] << " ";
            prev = arr[i];
        }
    }
}