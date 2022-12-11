/*
2628. 종이자르기
https://www.acmicpc.net/problem/2628
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


bool cmp(int a, int b){
    return a < b;
}


int main() {
    int width, height, cut_cnt;
    cin >> width >> height;
    cin >> cut_cnt;

    vector<int> width_vector, height_vector;
    width_vector.push_back(0);
    width_vector.push_back(width);
    height_vector.push_back(0);
    height_vector.push_back(height);

    for (int i=0; i<cut_cnt; i++){
        int type, position;
        cin >> type >> position;
        if (type == 0) height_vector.push_back(position);
        else width_vector.push_back(position);
    }

    int max_width = 0;
    int max_height = 0;
    sort(width_vector.begin(), width_vector.end(), cmp);
    sort(height_vector.begin(), height_vector.end(), cmp);
    for (int i=0; i<width_vector.size()-1; i++) max_width = max(max_width, width_vector[i+1] - width_vector[i]);
    for (int i=0; i<height_vector.size()-1; i++) max_height = max(max_height, height_vector[i+1] - height_vector[i]);

    cout << max_height * max_width << endl;
}