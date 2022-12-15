"""
20301. 반전 요세푸스
https://www.acmicpc.net/problem/20301
"""
from collections import deque


if __name__ == '__main__':
    N, K, M = map(int, input().split())
    D = deque()
    for i in range(N):
        D.append(i+1)

    job_count = 1
    right_flag = False
    while len(D) > 0:
        if (job_count-1) % (K*M) == 0:
            right_flag = not right_flag
            # print('right_flag change : {}'.format(right_flag))

        if job_count%K == 0:
            if right_flag:
                print(D.popleft())
            else:
                print(D.pop())
        else:
            if right_flag:
                D.append(D.popleft())
            else:
                D.appendleft(D.pop())
        # print(D)
        job_count += 1