#include <iostream>
using namespace std;

int sorted[8];

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
    int v[8] = {3, 6, 7, 1, 2, 4, 8, 5};
    merge_sort(v, 0, 7);
    for (int x : v) cout << x << " ";
}