/*
2866. 문자열 잘라내기
https://www.acmicpc.net/problem/2866
*/
#include <stdio.h>
#include <iostream>
#include <random>
using namespace std;

int array[1000000];
int sorted[1000000];

void merge(int *data, int start, int mid, int end){
    int i = start;
    int j = mid+1;
    int k = start;

    while (i <= mid || j <= end){
        if (j > end || (i <= mid && data[i] < data[j])){
            sorted[k] = data[i];
            i++;
        } else {
            sorted[k] = data[j];
            j++;
        }
        k++;
    }

    for (int k=start; k<=end; k++){
        data[k] = sorted[k];
    }
}

void merge_sort(int *data, int start, int end){
    if (start < end){
        int mid = (start + end) / 2;
        merge_sort(data, start, mid);
        merge_sort(data, mid+1, end);
        merge(data, start, mid, end);
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;
    cin >> N;
    for (int i=0; i<N; i++) cin >> array[i];
    // in_place_quick_sort(array, 0, N-1);
    merge_sort(array, 0, N-1);
    // for (int i=0; i<N; i++) cout << array[i] << endl;
    for (int i=0; i<N; i++) printf("%d\n", array[i]);
}