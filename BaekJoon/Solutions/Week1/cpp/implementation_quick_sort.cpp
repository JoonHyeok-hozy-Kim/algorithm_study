#include <iostream>
#include <random>
using namespace std;

void in_place_quick_sort(int * data, int start, int end){
    if (start < end){
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<int> dist_obj(start, end);

        int p = dist_obj(gen);
        int pivot = data[p];

        int temp = data[p];
        data[p] = data[end];
        data[end] = temp;

        
        int left = start;
        int right = end-1;

        while (left <= right){
            while (left <= right && data[left] < pivot) left++;
            while (left <= right && pivot < data[right]) right--;

            if (left <= right) {
                temp = data[left];
                data[left] = data[right];
                data[right] = temp;
                left++;
                right--;
            }
        }

        temp = data[left];
        data[left] = data[end];
        data[end] = temp;

        in_place_quick_sort(data, start, left-1);
        in_place_quick_sort(data, left+1, end);
    }
}

int main() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dist_obj(0, 99);
    int v[10];
    for (int i=0; i<10; i++) v[i] = dist_obj(gen);

    for (int x : v) cout << x << " ";
    cout << endl;

    in_place_quick_sort(v, 0, 9);
    
    for (int x : v) cout << x << " ";
    cout << endl;
}