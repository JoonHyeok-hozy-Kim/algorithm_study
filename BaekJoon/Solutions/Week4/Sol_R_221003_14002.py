"""
14002.
"""
from copy import deepcopy


if __name__ == '__main__':
    N = int(input())
    series = list(map(int, input().split()))
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

    len_max = None
    target = None
    for i in range(len(partials)):
        if len_max is None or len_max < len(partials[i]):
            len_max = len(partials[i])
            target = i
    print(len_max)
    print(*partials[target])

