"""
https://www.acmicpc.net/problem/1725
"""

from collections import deque


if __name__ == '__main__':
    N = int(input())
    histogram = [0]
    for _ in range(N):
        histogram.append(int(input()))
    histogram.append(0)
    # print(histogram)

    S = [0]
    result = 0
    for i in range(1, N+2):
        print('curr : {}'.format(histogram[i]))
        while len(S) > 0 and histogram[S[-1]] > histogram[i]:
            print('H : {}, S : {}'.format(histogram, S))
            prev = S.pop()
            print('temp : {} * ({} - {} - 1) = {}'.format(histogram[prev], i, S[-1], histogram[prev] * (i - S[-1] - 1)))
            result = max(result, histogram[prev] * (i - S[-1] - 1))
        S.append(i)

    print(result)
