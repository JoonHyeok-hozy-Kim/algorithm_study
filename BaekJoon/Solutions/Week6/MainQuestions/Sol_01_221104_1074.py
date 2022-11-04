"""
https://www.acmicpc.net/problem/1074
"""


def loop_search(N, r, c):
    istart, iend = 0, N
    jstart, jend = 0, N

    history = []
    while iend - istart > 1 or jend - jstart > 1:
        # print('i : {} ~ {}'.format(istart, iend))
        # print('j : {} ~ {}'.format(jstart, jend))
        # print()
        imid, jmid = (istart + iend) // 2, (jstart + jend) // 2

        if r < imid:
            if c < jmid:
                iend, jend = imid, jmid
                history.append(1)

            if c >= jmid:
                iend, jstart = imid, jmid
                history.append(2)

        if r >= imid:
            if c < jmid:
                istart, jend = imid, jmid
                history.append(3)

            if c >= jmid:
                istart, jstart = imid, jmid
                history.append(4)

    return history


if __name__ == '__main__':
    N, r, c = map(int, input().split())
    # print(N, r, c)

    H = loop_search(2**N, r, c)
    # print(H)

    P = 4**N
    result = 0
    for i in range(N):
        result += (H[i]-1) * P//4
        P //= 4
        # print('result : {}, P : {}'.format(result, P))

    print(result)