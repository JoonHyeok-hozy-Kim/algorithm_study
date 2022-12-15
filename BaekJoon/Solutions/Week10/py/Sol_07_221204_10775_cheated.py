"""
https://www.acmicpc.net/problem/10775
"""
input = __import__('sys').stdin.readline


def find(p, x):
    if p[x] == x:
        return x
    p[x] = find(p, p[x])
    return p[x]


def union(p, x, y):
    if x == y:
        return

    px, py = find(p, x), find(p, y)
    if px == py:
        return
    elif px < py:
        p[py] = px
    else:
        p[px] = py


if __name__ == '__main__':
    G = int(input())
    P = int(input())
    gates = [g for g in range(G+1)]
    docked = [False] * (G+1)
    docked_cnt = 0
    for p in range(P):
        gi = int(input())
        gi_found = find(gates, gi)
        while docked[gi_found]:
            union(gates, gi_found, gi_found-1)
            gi_found = find(gates, gi_found-1)

        # print('gates : {}'.format(gates))
        # print('docked : {}'.format(docked))
        # print('gi_found : {}'.format(gi_found))
        if gi_found == 0:
            break
        else:
            docked[gi_found] = True
            union(gates, gi_found, gi_found-1)
            docked_cnt += 1

    print(docked_cnt)