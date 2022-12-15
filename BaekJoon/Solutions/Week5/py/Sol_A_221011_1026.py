"""
1026. 보물
https://www.acmicpc.net/problem/1026
"""


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    result = 0
    A.sort()
    B.sort()
    # print(A, B)

    for i in range(N):
        result += A[i] * B[N-1-i]

    print(result)