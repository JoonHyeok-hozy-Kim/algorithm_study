#include <iostream>
#include <vector>
using namespace std;

void set_zero(vector<vector<int>> &V){
    for (int i=0; i<V.size(); i++){
        for (int j=0; j<V.size(); j++){
            V[i][j] = 0;
        }
    }
}

void zero(vector<vector<int>> &V){
    for (int i=0; i<V.size(); i++){
        for (int j=0; j<V.size(); j++){
            if (V[i][j] == 0){
                set_zero(V);
                return;
            }
        }
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


int main(){
    vector<vector<int>> mat1 = {{1,2,3}, {4,5,6}, {7,8,9}};

    zero(mat1);
    show_matrix(mat1);

    vector<vector<int>> mat2 = {{1,2,3}, {4,0,6}, {7,8,9}};

    zero(mat2);
    show_matrix(mat2);
}