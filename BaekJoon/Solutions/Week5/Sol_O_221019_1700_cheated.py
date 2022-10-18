"""
1700. 멀티탭 스케줄링
https://www.acmicpc.net/problem/1700
"""
from heapq import heapify, heappop, heappush


if __name__ == '__main__':
    N, K = map(int, input().split())
    usage_list = list(map(int, input().split()))
    # print(usage_list)

    usage_cnt = [0] * (K+1)
    for i in usage_list:
        usage_cnt[i] += 1
    # print(usage_cnt)

    plug_out_cnt = 0
    consent = []
    idx = 0
    while len(consent) < N:
        usage_cnt[usage_list[idx]] -= 1
        if usage_list[idx] not in consent:
            consent.append(usage_list[idx])
        idx += 1
    # print(consent)

    while idx < len(usage_list):
        if usage_list[idx] not in consent:
            future_usage = [K] * N
            for j in range(N):
                for k in range(idx, K):
                    if usage_list[k] == consent[j]:
                        future_usage[j] = k
                        break
            max_consent = future_usage.index(max(future_usage))
            consent[max_consent] = usage_list[idx]
            plug_out_cnt += 1

        usage_cnt[usage_list[idx]] -= 1
        idx += 1
        # print(consent)

    print(plug_out_cnt)