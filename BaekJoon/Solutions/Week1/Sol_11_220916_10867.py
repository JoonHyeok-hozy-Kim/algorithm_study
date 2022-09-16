"""
10867. 중복 빼고 정렬하기

N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.
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