/*
2750. 수 정렬하기
https://www.acmicpc.net/problem/2750
*/
#include <iostream>
using namespace std;

int array[1000];
int sort_temp[1000];

void _merge(int * data, int start, int mid, int end){
    int i1 = start;
    int i2 = mid+1;
    int j = start;

    while (i1 <= mid || i2 <= end){
        if (i2 > end || (i1 <= mid && data[i1] < data[i2])){
            sort_temp[j] = data[i1];
            i1++;
        } else {
            sort_temp[j] = data[i2];
            i2++;
        }
        j++;
    }

    for (int k=start; k<=end; k++){
        array[k] = sort_temp[k];
    }
}

void merge_sort(int * data, int start, int end){
    if (start < end){
        int mid = (start + end) / 2;
        merge_sort(data, start, mid);
        merge_sort(data, mid+1, end);
        _merge(data, start, mid, end);
    }
}

int main() {
    int N;
    cin >> N;

    for (int i=0; i<N; i++){
        cin >> array[i];
    }

    merge_sort(array, 0, N-1);

    for (int i=0; i<N; i++){
        cout << array[i] << endl;
    }
}