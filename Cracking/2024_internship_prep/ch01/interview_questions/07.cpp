#include <iostream>
#include <vector>
using namespace std;

void rotate(vector<vector<int>> &V){
    int left = 0;
    int right = V.size() - 1;
    int top, bottom;
    int top_left;
    
    while (left < right) {
        top = left;
        bottom = right;
        
        for (int i = 0; i< right-left; i++){
            top_left = V[top][left + i];
            
            V[top][left + i] = V[bottom - i][left];
            V[bottom - i][left] = V[bottom][right - i];
            V[bottom][right - i] = V[top + i][right];
            V[top + i][right] = top_left;
        }
        
        left++;
        right--;
    }
} 

void show_matrix(vector<vector<int>> &V){
    for (vector<int> vec : V){
        cout << "| ";
        for (int i : vec){
            cout << i << " ";
        }
        cout << "|\n";
    }
    cout << endl;
}


int main() {
    vector<vector<int>> mat1 = {{1,2,3}, {4,5,6}, {7,8,9}};

    show_matrix(mat1);
    rotate(mat1);
    show_matrix(mat1);
}