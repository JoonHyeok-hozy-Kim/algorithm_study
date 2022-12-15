#include <iostream>
#include <algorithm>
using namespace std;

int area[250000];

int main() {
    int N, M, B;
    cin >> N >> M >> B;

    int idx=0;
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++){
            if (j < M-1){
                scanf("%d ", &(area[idx]));
            } else {
                scanf("%d", &(area[idx]));
            }
            idx++;
        }
    }
    // for (int i=0; i<N*M; i++) cout << area[i] << " ";

    sort(area, area+N*M);
    // for (int i=0; i<N*M; i++) cout << area[i] << " ";

    int min_time_spent = NULL;
    int result_height;
    int temp_time_spent;
    int inventory;
    bool skip;
    for (int h=area[N*M-1]; h>=area[0]; h--){
        inventory = B;
        temp_time_spent = 0;
        skip = false;
        for (int i=N*M-1; i>=0; i--) {
            if (min_time_spent != NULL && temp_time_spent > min_time_spent) {
                skip = true;
                break;
            }

            if (area[i] > h) {
                inventory += area[i] - h;
                temp_time_spent += (area[i] - h) * 2;
            } else if (area[i] < h) {
                inventory -= h - area[i];
                if (inventory < 0) {
                    skip = true;
                    break;
                }
                temp_time_spent += h - area[i];
            }
        }

        if (!skip){
            if (min_time_spent == NULL || min_time_spent > temp_time_spent) {
                min_time_spent = temp_time_spent;
                result_height = h;
            } else if (min_time_spent == temp_time_spent) {
                result_height = max(result_height, h);
            }
        }
    }

    printf("%d %d", min_time_spent, result_height);
}