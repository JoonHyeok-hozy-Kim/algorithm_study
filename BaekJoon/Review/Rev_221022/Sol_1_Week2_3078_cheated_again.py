"""
https://www.acmicpc.net/problem/3078
"""

from collections import deque


if __name__ == '__main__':
    N, K = map(int, input().split())
    students = [len(input()) for _ in range(N)]
    result = 0
    # print(students)

    peer_map = {}
    for i in range(1, K):
        if students[i] not in peer_map:
            peer_map[students[i]] = 0
        peer_map[students[i]] += 1

    for j in range(N-1):
        if j+K < N:
            if students[j+K] not in peer_map:
                peer_map[students[j+K]] = 0
            peer_map[students[j+K]] += 1
        # print(students[j], Q)
        if students[j] in peer_map:
            result += peer_map[students[j]]

        if students[j+1] in peer_map:
            peer_map[students[j+1]] -= 1


    print(result)