"""
10867. 중복 빼고 정렬하기
https://www.acmicpc.net/problem/10867
"""


if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))
    M = {}
    for i in range(N):
        M[L[i]] = L[i]
    L = list(M.keys())
    L.sort()
    for i in L:
        print(i, end=" ")