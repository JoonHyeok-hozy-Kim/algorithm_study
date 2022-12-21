#include <iostream>
using namespace std;

typedef long long ll;

int * name_lens;

int main() {
    int N, K;
    cin >> N >> K;

    name_lens = (int *) malloc(N * sizeof(int));
    string temp_string;
    for (int i=0; i<N; i++){        
        cin >> temp_string;
        name_lens[i] = temp_string.length();
    }
    
    ll good_friends = 0;
    ll len_array[21] = {};
    // for (int i=0; i<21; i++) printf("%d ", len_array[i]);

    for (int i=0; i<K; i++){
        // len_array[name_lens[i]] += 1;
        len_array[name_lens[i]] += 1;
    }

    for (int i=0; i<N; i++){
        if (i-K-1 >= 0){
            len_array[name_lens[i-K-1]]--;
        }

        if (i+K < N){
            len_array[name_lens[i+K]]++;
        }

        good_friends += len_array[name_lens[i]] - 1;
    }
    
    cout << good_friends/2 << endl;
}