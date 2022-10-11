"""
11047. 동전 0
https://www.acmicpc.net/problem/11047
"""

if __name__ == '__main__':
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]

    cnt = 0
    for c in reversed(coins):
        k = K//c
        if k > 0:
            cnt += k
            K %= c

    print(cnt)