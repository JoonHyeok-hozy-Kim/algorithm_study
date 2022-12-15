"""
https://www.acmicpc.net/problem/23749
"""
from collections import deque


def win(N, D):
    compare = [None, None]
    scores = [0, 0]
    for i in range(N*2):
        if i%2 == 0:
            compare[0] = D%2
            D //= 2
        elif i%2 == 1:
            compare[1] = D%2
            if compare[0] > compare[1]:
                scores[0] += 1
            elif compare[0] < compare[1]:
                scores[1] += 1
            D //= 2
        # print(scores)
    if scores[1] > scores[0]:
        return True
    else:
        return False


def operate(N, D, i):
    result = 0
    if D & (1<<(N*2-1-i)):
        result += 1

    for j in range(N*2):
        if j != i:
            result *= 2
            if D & (1<<(N*2-1-j)):
                result += 1

    return result


def display_deck(N, D):
    result = []
    for j in range(N*2):
        if D & (1<<(N*2-1-j)):
            result.append('O')
        else:
            result.append('X')
    print(*result, sep=" ")


def bfs(N, D):
    if win(N, D):
        return 0

    Q = deque()
    Q.append([0, D])
    while Q:
        prev_cnt, popped = Q.popleft()
        for i in range(N*2-1):
            new_deck = operate(N, popped, i+1)
            # display_deck(N, new_deck)
            if win(N, new_deck):
                return prev_cnt + 1
            else:
                Q.append([prev_cnt+1, new_deck])
        # print(Q)


if __name__ == '__main__':
    N = int(input())
    binary_deck = 0
    for card in map(str, input().split()):
        # print(card)
        binary_deck *= 2
        if card == 'O':
            binary_deck += 1
    # print(bin(binary_deck))

    # print(win(N, binary_deck))
    # display_deck(N, binary_deck)
    # for i in range(1, 4):
    #     new_deck = operate(N, binary_deck, i)
    #     display_deck(N, new_deck)

    print(bfs(N, binary_deck))