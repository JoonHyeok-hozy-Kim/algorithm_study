"""
https://www.acmicpc.net/problem/24391
"""
from collections import deque


def get_connected_sets(N, M):
    set_id = 0
    dp = [None] * (N+1)
    for k in M.keys():
        if dp[k] is None:
            if dfs(M, k, dp, set_id) > 0:
                set_id += 1
    return dp


def dfs(M, i, dp, set_id):
    Q = deque()
    Q.append(i)
    insert_cnt = 0
    while Q:
        popped = Q.popleft()
        if dp[popped] is None:
            dp[popped] = set_id
            insert_cnt += 1
            for j in M[popped]:
                Q.append(j)

    return insert_cnt



if __name__ == '__main__':
    N, M = map(int, input().split())
    linked_map = {}
    for _ in range(M):
        i, j = map(int, input().split())
        if i not in linked_map:
            linked_map[i] = set()
        linked_map[i].add(j)

        if j not in linked_map:
            linked_map[j] = set()
        linked_map[j].add(i)
    # print('linked_map : {}'.format(linked_map))

    dp = get_connected_sets(N, linked_map)
    # print('dp : {}'.format(dp))

    schedule = list(map(int, input().split()))
    # print(schedule)

    result = 0
    course = schedule[0]
    for c in range(1, len(schedule)):
        if dp[course] is not None and dp[schedule[c]] is not None and dp[course] == dp[schedule[c]]:
            continue
        else:
            result += 1
            course = schedule[c]

    print(result)



"""
5 3
1 2
2 5
3 4
1 2 3 5 4

5 3
1 2
2 3
3 4
1 4 3 2 5

5 3
1 2
3 4
4 1
1 2 3 4 5

6 4
1 2
3 4
4 1
5 6
1 2 3 4 5 6

7 4
1 2
3 4
4 1
7 6
1 2 3 4 5 6 7

6 5
1 2
2 3
3 4
5 6
6 1
1 2 3 4 5 6

6 5
1 2
3 4
5 6
1 3
3 5
1 2 3 4 5 6
"""