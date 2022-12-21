"""
3078. 좋은 친구

https://www.acmicpc.net/problem/3078
"""
# from collections import deque

# if __name__ == '__main__':
#     N, K = map(int, input().split())
#     Q = [deque() for _ in range(21)]
#     result = 0
#     for i in range(N):
#         in_len = len(input())
#         while len(Q[in_len]) > 0 and (i - Q[in_len][0] > K):
#             Q[in_len].popleft()
#         result += len(Q[in_len])
#         Q[in_len].append(i)
#     print(result)


if __name__ == '__main__':
    N, K = map(int, input().split())
    students = [len(input()) for _ in range(N)]

    dp = [0 for _ in range(21)]
    for i in range(K):
        dp[students[i]] += 1
    
    good_friend = 0
    for i in range(N):
        dp[students[i]] -= 1

        if i+K < N:
            dp[students[i+K]] += 1
        
        good_friend += dp[students[i]]
    
    print(good_friend)