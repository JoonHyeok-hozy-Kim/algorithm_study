"""
https://www.acmicpc.net/problem/1208
"""
from bisect import bisect_left, bisect_right


if __name__ == '__main__':
    N, S = map(int, input().split())
    series = list(map(int, input().split()))
    # print(series)

    pt1 = series[:N//2]
    pt2 = series[N//2:]
    # print(pt1)
    # print(pt2)

    sum1 = [0] * (2**(N//2))
    sum2 = [0] * (2**(N - N//2))

    for i in range(2**(N//2)):
        for j in range(N//2):
            if i & (1<<j):
                sum1[i] += pt1[j]


    for i in range(2**(N - N//2)):
        for j in range(N - N//2):
            if i & (1<<j):
                sum2[i] += pt2[j]

    sum1.pop(0)
    sum2.pop(0)

    sum1.sort()
    sum2.sort()

    # print(sum1)
    # print(sum2)

    result = 0
    for i in range(len(sum1)):
        if sum1[i] == S:
            # print('pt1, sum1[i] : {}'.format(sum1[i]))
            result += 1
        temp = bisect_left(sum2, S-sum1[i])
        if temp < len(sum2) and sum1[i] + sum2[temp] == S:
            # print('pt2 i : {}, temp : {}'.format(i, temp))
            result += bisect_right(sum2, S-sum1[i]) - temp
        # print(result)

    for i in range(len(sum2)):
        if sum2[i] == S:
            result += 1

    print(result)

