"""
https://www.acmicpc.net/problem/17833
"""
from heapq import heappop, heappush
from math import inf


def validate_sample_usage(N, sample, entering_height, i1=True):
    if i1:
        return sample[2] <= entering_height and entering_height + (sample[0] - sample[2]) <= N
    else:
        return sample[3] <= entering_height and entering_height + (sample[0] - sample[3]) <= N


def time_heap_solution(N, R, D, S):
    heap = []
    heappush(heap, (0, R))    # total_time_spent, entering_height
    heights_reached = [inf] * (N+1)
    result_candidate = None
    while heap:
        popped = heappop(heap)
        if popped[1] == D:
            result_candidate = min(result_candidate, popped[0]) if result_candidate is not None else popped[0]

        for s in S:
            if (result_candidate is None) or (result_candidate is not None and popped[0] + s[1] < result_candidate):
                if validate_sample_usage(N, s, popped[1], True):
                    if heights_reached[popped[1]+s[3]-s[2]] > popped[0]+s[1]:
                        heights_reached[popped[1]+s[3]-s[2]] = popped[0]+s[1]
                        heappush(heap, (popped[0]+s[1], popped[1]+s[3]-s[2]))
                if validate_sample_usage(N, s, popped[1], False):
                    if heights_reached[popped[1]+s[2]-s[3]] > popped[0]+s[1]:
                        heights_reached[popped[1]+s[2]-s[3]] = popped[0]+s[1]
                        heappush(heap, (popped[0]+s[1], popped[1]+s[2]-s[3]))
        # print('heap : {}'.format(heap))
        # print('heights_reached : {}'.format(heights_reached))

    if result_candidate is not None:
        return result_candidate
    else:
        return -1

if __name__ == '__main__':
    N = int(input())
    R, D = map(int, input().split())
    M = int(input())
    samples = [list(map(int, input().split())) for _ in range(M)]
    samples.sort()
    # print(samples)    # [H_i, T_i, E_i1, E_i2]

    result = time_heap_solution(N, R, D, samples)
    print(result)