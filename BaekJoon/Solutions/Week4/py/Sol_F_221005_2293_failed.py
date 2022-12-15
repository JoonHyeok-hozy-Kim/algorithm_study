"""
2293. 동전 1
https://www.acmicpc.net/problem/2293
"""
from copy import deepcopy

def get_sum(C, U):
    result = 0
    for i in range(len(C)):
        result += C[i] * U[i]
    return result


def over_max(M, U):
    for i in range(len(M)):
        if M[i] < U[i]:
            return True
    return False


def recursive_cnt(C, K, M, usage_cnt=None, j=0):
    # print('In recursive_cnt, usage_cnt : {}'.format(usage_cnt))
    if usage_cnt is None:
        usage_cnt = [0] * len(C)

    sum_check = get_sum(C, usage_cnt)
    if sum_check == K:
        # print('-> FOUND with {}'.format(usage_cnt))
        return 1
    elif sum_check > K or j >= len(C) or over_max(M, usage_cnt):
        return 0

    temp_cnt = 0
    for k in range(M[j]+1):
        c_usage = deepcopy(usage_cnt)
        # print('COPY usage : {}'.format(c_usage))
        temp_cnt += recursive_cnt(C, K, M, c_usage, j+1)
        usage_cnt[j] += 1

    return temp_cnt


def factorial_solution(C, K):
    max_usages = []
    for c in C:
        max_usages.append(K//c)

    return recursive_cnt(C, K, max_usages)


if __name__ == '__main__':
    N, K = map(int, input().split())
    coins = []
    for i in range(N):
        coins.append(int(input()))
    # coins.sort()
    # print(coins)

    # print(factorial_solution(coins, K))