"""
https://www.acmicpc.net/problem/4195
"""
input = __import__('sys').stdin.readline


def find(p, x):
    if p[x] == x:
        return x

    p[x] = find(p, p[x])
    return p[x]


def union(p, s, x, y):
    if x == y:
        return

    px, py = find(p, x), find(p, y)
    if py == px:
        return

    new_size = s[px] + s[py]
    if px < py:
        p[py] = px
    else:
        p[px] = py

    s[px] = s[py] = new_size


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        F = int(input())
        id = 0
        friends = {}
        parents = []
        size = []
        for _ in range(F):
            name1, name2 = input().split()
            if name1 not in friends:
                friends[name1] = id
                parents.append(id)
                size.append(1)
                id += 1
            if name2 not in friends:
                friends[name2] = id
                parents.append(id)
                size.append(1)
                id += 1
            union(parents, size, friends[name1], friends[name2])
            # print('friends : {}'.format(friends))
            # print('parents : {}'.format(parents))
            # print('size : {}'.format(size))
            parent = find(parents, friends[name1])
            print(size[parent])

"""
1
9
a b
c d
e f
g h
b c
f g
d e
h a
b g
"""