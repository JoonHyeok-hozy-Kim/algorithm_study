"""
https://www.acmicpc.net/problem/2776
"""


def binary_search(A, v):
    start, end = 0, len(A)-1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] >= v:
            end = mid-1
        else:
            start = mid+1
    return start


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        memo1 = list(map(int, input().split()))
        memo1.sort()
        M = int(input())
        for num in map(int, input().split()):
            idx = binary_search(memo1, num)
            if idx < len(memo1) and memo1[idx] == num:
                print(1)
            else:
                print(0)
