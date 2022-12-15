"""
18115. 카드 놓기
https://www.acmicpc.net/problem/18115
"""
from collections import deque

def trick_one_reverse(result, hand):
    hand.appendleft(str(result.popleft()))

def trick_two_reverse(result, hand):
    top_at_hand = hand.popleft()
    hand.appendleft(str(result.popleft()))
    hand.appendleft(top_at_hand)

def trick_three_reverse(result, hand):
    hand.append(str(result.popleft()))

def trick_reverse(result, hand, num):
    if num == 1:
        trick_one_reverse(result, hand)
    elif num == 2:
        trick_two_reverse(result, hand)
    elif num == 3:
        trick_three_reverse(result, hand)
    # print('Result : {}, Hand : {}'.format(result, hand))

if __name__ == '__main__':
    N = int(input())
    trick_list = list(map(int, input().split()))
    t = len(trick_list)

    hand = deque()
    result = deque()
    for i in range(N):
        result.append(i+1)
    # print(result)
    for i in range(t):
        trick_reverse(result, hand, trick_list[t-1-i])

    print(' '.join(hand))