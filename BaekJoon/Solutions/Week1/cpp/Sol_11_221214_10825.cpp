#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <tuple>
using namespace std;

int N;
// vector<tuple<string, int, int, int>> vec;
tuple<string, int, int, int> arr[1000000];

bool compare(tuple<string, int, int, int> t1, tuple<string, int, int, int> t2){
    if (get<1>(t1) > get<1>(t2)){
        return true;
    } else if (get<1>(t1) < get<1>(t2)){
        return false;
    } else {
        if (get<2>(t1) < get<2>(t2)){
            return true;
        } else if (get<2>(t1) > get<2>(t2)){
            return false;
        } else {
            if (get<3>(t1) > get<3>(t2)){
                return true;
            } else if (get<3>(t1) < get<3>(t2)){
                return false;
            } else {
                return get<0>(t1) < get<0>(t2);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> N;
    // vec.reserve(N);
    
    string name;
    int kor, eng, math;
    for(int i=0; i<N; i++){
        cin >> name >> kor >> eng >> math;
        // vec.push_back(make_tuple(name, kor, eng, math));
        arr[i] = make_tuple(name, kor, eng, math);
    }

    // sort(vec.begin(), vec.end(), compare);
    sort(arr, arr+N, compare);

    for (int i=0; i<N; i++){
        // cout << get<0>(vec[i]) << endl;
        cout << get<0>(arr[i]) << '\n';
    }
}