"""
11053. 가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
"""
from copy import deepcopy


if __name__ == '__main__':
    N = int(input())
    series = list(map(int, input().split()))
    # N = 10
    # series = [1, 2, 1, 2, 3, 0, 1, 2, 3, 4]
    partials = [[series[0]]]

    for i in range(1, N):
        max_prev = None
        for j in range(i):
            if series[j] < series[i]:
                max_prev = partials[j] if max_prev is None or len(max_prev) < len(partials[j]) else max_prev
        if max_prev is not None:
            new_partial = deepcopy(max_prev)
            new_partial.append(series[i])
        else:
            new_partial = [series[i]]
        partials.append(new_partial)

    # print(series)
    # print(partials)

    result = 0
    for k in partials:
        result = max(result, len(k))
    print(result)