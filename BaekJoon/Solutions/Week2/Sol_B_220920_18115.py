"""
18115. 카드 놓기

수현이는 카드 기술을 연습하고 있다. 수현이의 손에 들린 카드를 하나씩 내려놓아 바닥에 쌓으려고 한다. 수현이가 쓸 수 있는 기술은 다음 3가지다.

1. 제일 위의 카드 1장을 바닥에 내려놓는다.
2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.

수현이는 처음에 카드 N장을 들고 있다. 카드에는 1부터 N까지의 정수가 중복되지 않게 적혀 있다. 기술을 N번 사용하여 카드를 다 내려놓았을 때,
놓여 있는 카드들을 확인했더니 위에서부터 순서대로 1, 2, …, N이 적혀 있었다!

놀란 수현이는 처음에 카드가 어떻게 배치되어 있었는지 궁금해졌다. 처음 카드의 상태를 출력하여라.
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