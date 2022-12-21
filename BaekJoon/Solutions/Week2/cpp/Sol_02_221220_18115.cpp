/*
카드 놓기
https://www.acmicpc.net/problem/18115
*/

#include <iostream>
#include <deque>
using namespace std;

typedef deque<int> di;

int * skill_history;

int main() {
    int N;
    scanf("%d\n", &N);
    skill_history = (int *) malloc(N * sizeof(int));
    
    di result_deck;
    for (int i=0; i<N; i++){
        scanf(" %d", &skill_history[i]);
        result_deck.push_back(i+1);
    }
    // for (int i=0; i<N; i++) printf("%d ", skill_history[i]);

    di original_deck;
    int card;
    int temp;
    for (int i=N-1; i>=0; i--){
        card = result_deck.front();
        result_deck.pop_front();
        if (skill_history[i] == 1){
            original_deck.push_front(card);
        } else if (skill_history[i] == 2) {
            temp = original_deck.front();
            original_deck.pop_front();
            original_deck.push_front(card);
            original_deck.push_front(temp);
        } else {
            original_deck.push_back(card);
        }
    }

    for (int i=0; i<N; i++){
        printf("%d ", original_deck[i]);
    }
}