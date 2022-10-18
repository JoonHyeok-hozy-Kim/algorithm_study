"""
11497. 통나무 건너뛰기
https://www.acmicpc.net/problem/11497
"""


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        logs = list(map(int, input().split()))
        logs.sort()
        result = [None] * N
        for i in range(N):
            if i % 2 == 0:
                result[i//2] = logs[i]

            else:
                result[(i//2+1)*(-1)] = logs[i]
        # print(result)

        difficulty = None
        for i in range(N):
            temp_diff = max(abs(result[i] - result[i-1]), abs(result[(i+1)%N] - result[i]))
            if difficulty is None or temp_diff > difficulty:
                difficulty = temp_diff
        print(difficulty)