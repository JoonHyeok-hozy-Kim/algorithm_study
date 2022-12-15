"""
https://www.acmicpc.net/problem/11724
"""

def dfs(V, E, N, i):
    if i in E:
        for j in E[i].keys():
            if j in V:
                if V[j]:
                    N[j] = True
                    V[j] = False
                    dfs(V, E, N, j)


if __name__ == '__main__':
    N, M = map(int, input().split())
    v_not_used = {}
    for i in range(1, N+1):
        v_not_used[i] = True

    edges = {}
    for i in range(M):
        u, v = map(int, input().split())

        if u not in edges:
            edges[u] = {}
        edges[u][v] = True

        if v not in edges:
            edges[v] = {}
        edges[v][u] = True

    # print(v_not_used)
    # print(edges)

    cnt = 0
    for v in v_not_used:
        if v_not_used[v]:
            new_component = {}
            new_component[v] = True
            v_not_used[v] = False
            dfs(v_not_used, edges, new_component, v)
            # print(new_component)
            cnt += 1

    print(cnt)