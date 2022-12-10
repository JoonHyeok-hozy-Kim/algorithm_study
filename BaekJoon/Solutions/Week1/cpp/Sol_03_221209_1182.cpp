//1182. 부분수열의 합
//https://www.acmicpc.net/problem/1182

#include <iostream>

const int s_size = 2000000;
const int dp_size = s_size*2+1;
int dp[dp_size] = {};


int val_to_idx(int val){
    return val + s_size;
}

int idx_to_val(int idx){
    return idx - s_size;
}


int main(){
    int N, S;
    std::cin >> N >> S;
    
    int array[20];
    for (int i=0; i<N; i++){
        std::cin >> array[i];
    }

    // for (int j : array) std::cout << j << " ";
    
    dp[val_to_idx(array[0])] = 1;
    // for (int x : dp) std::cout << x << " ";
    // std::cout << std::endl;
    
    // std::cout << dp_size << std::endl;

    for (int i=1; i<N; i++){
        if (array[i] < 0){
            for (int j=0; j<dp_size; j++){
                if (dp[j] > 0) {
                    if (j+array[i] < dp_size && j+array[i] >= 0) dp[j+array[i]] += dp[j];
                }                
            }
        }

        else{
            for (int j=dp_size-1; j>=0; j--){
                if (dp[j] > 0) {
                    if (j+array[i] < dp_size && j+array[i] >= 0) dp[j+array[i]] += dp[j];
                }                
            }
        }
        
        dp[val_to_idx(array[i])] += 1;

        // for (int x : dp) std::cout << x << " ";
        // std::cout << std::endl;
    }

    std::cout << dp[val_to_idx(S)] << std::endl;
    

    return 0;
}