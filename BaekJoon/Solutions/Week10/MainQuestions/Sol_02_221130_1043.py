"""
https://www.acmicpc.net/problem/1043
"""


def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]


def union(p, x, y):
    if x == y:
        return
    px, py = find(p, x), find(p, y)
    if px < py:
        p[py] = px
    else:
        p[px] = py


if __name__ == '__main__':
    N, M = map(int, input().split())
    parents = [i for i in range(N+1)]   # The ones who know the truth will have parent 0
    init = True
    for i in map(int, input().split()):
        if init:
            init = False
            continue
        parents[i] = 0
    # print('Initial, parents : {}'.format(parents))

    party_min_members = [None] * M
    for j in range(M):
        members = list(map(int, input().split()))
        member_cnt = members.pop(0)
        for k in range(member_cnt-1):
            union(parents, members[k], members[k+1])

        party_min_members[j] = parents[members[0]]
        # print('party {}, parents : {}'.format(j, parents))

    for i in range(1, N+1):
        find(parents, i)
    # print('party {}, parents : {}'.format(j, parents))

    result = 0
    for m in party_min_members:
        if find(parents, m) > 0:
            result += 1
    print(result)