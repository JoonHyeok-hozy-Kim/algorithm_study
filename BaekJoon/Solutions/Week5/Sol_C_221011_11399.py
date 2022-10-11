"""
11399. ATM
https://www.acmicpc.net/problem/11399
"""



if __name__ == '__main__':
    N = int(input())
    Q = list(map(int, input().split()))
    Q.sort()

    result = 0
    for i in range(N):
        result += Q[i]*(N-i)

    print(result)