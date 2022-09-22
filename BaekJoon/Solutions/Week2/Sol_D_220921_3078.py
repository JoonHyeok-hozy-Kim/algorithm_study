"""
3078. 좋은 친구

https://www.acmicpc.net/problem/3078
"""
from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    Q = [deque() for _ in range(21)]
    result = 0
    for i in range(N):
        in_len = len(input())
        while len(Q[in_len]) > 0 and (i - Q[in_len][0] > K):
            Q[in_len].popleft()
        result += len(Q[in_len])
        Q[in_len].append(i)
    print(result)