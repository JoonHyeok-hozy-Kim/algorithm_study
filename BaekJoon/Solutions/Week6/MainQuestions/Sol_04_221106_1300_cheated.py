"""
https://www.acmicpc.net/problem/1300
"""


if __name__ == '__main__':
    N = int(input())
    k = int(input())

    start, end = 0, N**2
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(N):
            cnt += min(N, mid//(i+1))

        if cnt >= k:
            end = mid-1
        else:
            start = mid+1

    print(start)