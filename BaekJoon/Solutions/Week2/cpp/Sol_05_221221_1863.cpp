#include <iostream>
#include <stack>
using namespace std;

int * changes;
stack<int> prev_heights;

int main() {
    int N;
    scanf("%d", &N);

    changes = (int *) malloc(N * sizeof(int));
    int * temp;
    for (int i=0; i<N; i++){
        scanf("%d %d", &temp, &changes[i]);
    }
    // for (int i=0; i<N; i++) printf("%d ", changes[i]);

    int result = 0;
    for (int i=0; i<N; i++){
        if (changes[i] == 0){
            while (prev_heights.size()){
                prev_heights.pop();
                result++;
            }
        } else if (prev_heights.size() == 0){
            prev_heights.push(changes[i]);
        } else {
            if (prev_heights.top() < changes[i]){
                prev_heights.push(changes[i]);
            } else {
                while (prev_heights.size() > 0 && prev_heights.top() > changes[i]){
                    prev_heights.pop();
                    result++;
                }

                if (prev_heights.size() == 0 || prev_heights.top() < changes[i]){
                    prev_heights.push(changes[i]);
                }
            }
        }
        // printf("changes[%d] : %d, result : %d\n", i, changes[i], result);
    }

    while (prev_heights.size() > 0){
        // printf("prev_heights.top() : %d", prev_heights.top());
        prev_heights.pop();
        result++;
        // printf(", result : %d\n", result);
    }

    printf("%d\n", result);
}