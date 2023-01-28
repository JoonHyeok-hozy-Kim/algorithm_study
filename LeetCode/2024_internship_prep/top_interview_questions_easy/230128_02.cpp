#include <vector>
#include <unordered_set>
using namespace std;

bool isValidSudoku(vector<vector<char>>& board) {
    int i, j, n, k;
    unordered_set<char> S;
    
    for (i=0; i<9; i++){
        for (n=0; n<9; n++){
            if (board[i][n] != '.'){
                if (S.find(board[i][n]) == S.end()){
                    S.insert(board[i][n]);
                } else {
                    return false;
                }
            }
        }
        S.clear();
    }
    
    for (j=0; j<9; j++){
        for (k=0; k<9; k++){
            if (board[k][j] != '.'){
                if (S.find(board[k][j]) == S.end()){
                    S.insert(board[k][j]);
                } else {
                    return false;
                }
            }
        }
        S.clear();
    }
    
    for (i=0; i<3; i++){
        for (j=0; j<3; j++){
            for (n=0; n<3; n++){
                for (k=0; k<3; k++){
                    if (board[3*i+n][3*j+k] != '.'){
                        if (S.find(board[3*i+n][3*j+k]) == S.end()){
                            S.insert(board[3*i+n][3*j+k]);
                        } else {
                            return false;
                        }
                    }
                }
            }
            S.clear();
        } 
    }
    
    return true;
}