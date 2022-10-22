"""
https://www.acmicpc.net/problem/18115
"""
from collections import deque


if __name__ == '__main__':
    N = int(input())
    skills = list(map(int, input().split()))
    # print(skills)

    deck = deque()
    card = 1
    for s in reversed(skills):
        if s == 1:
            deck.appendleft(card)

        elif s == 2:
            temp = deck.popleft()
            deck.appendleft(card)
            deck.appendleft(temp)

        else:
            deck.append(card)

        card += 1

    print(*deck, sep=" ")