"""
2293. 동전 1
https://www.acmicpc.net/problem/2293
"""

def recursive_trial(C, M, K, i=0, temp_sum=0):
    if temp_sum == K:
        return 1
    elif temp_sum > K:
        return 0

    temp_cnt = 0
    for j in range(M[i]):
        temp_sum += C[i]



if __name__ == '__main__':
    N, K = map(int, input().split())
    coins = []
    for i in range(N):
        coins.append(int(input()))
    coins.sort()
    # print(coins)

    max_usages = []
    for c in coins:
        max_usages.append(K//c)
    print(max_usages)