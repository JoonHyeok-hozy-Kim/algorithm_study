"""
20301. 반전 요세푸스

요세푸스 문제는 다음과 같다.

1번 사람 오른쪽에는 2번 사람이 앉아 있고, 2번 사람 오른쪽에는 3번 사람이 앉아 있고, 계속하여 같은 방식으로 N명의 사람들이 원을 이루며
앉아 있다. N번 사람 오른쪽에는 1번 사람이 앉아 있다. 이제 K(<= N)번 사람을 우선 제거하고, 이후 직전 제거된 사람의 오른쪽의
K번째 사람을 계속 제거해 나간다. 모든 사람이 제거되었을 때, 제거된 사람의 순서는 어떻게 될까?

이 문제의 답을 (N,K,M)–요세푸스 순열이라고 하며, (7,3)–요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>가 된다.

하지만 한 방향으로만 계속 돌아가는 건 너무 지루하다. 따라서 요세푸스 문제에 재미를 더하기 위해 M명의 사람이 제거될 때마다 원을 돌리는
방향을 계속해서 바꾸려고 한다. 이렇게 정의된 새로운 문제의 답을 (N, K, M)–반전 요세푸스 순열이라고 하며, (7,3,4)–반전 요세푸스 순열은
<3, 6, 2, 7, 1, 5, 4>가 된다.

N,K,M이 주어질 때, (N,K,M)–반전 요세푸스 순열을 계산해 보자.
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