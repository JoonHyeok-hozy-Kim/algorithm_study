"""
https://www.acmicpc.net/problem/25319
"""


def find_route(a, b):
    # print('find_route')
    result = []
    for _ in range(abs(a[0] - b[0])):
        if a[0] > b[0]:
            result.append('U')
        else:
            result.append('D')

    for _ in range(abs(a[1] - b[1])):
        if a[1] > b[1]:
            result.append('L')
        else:
            result.append('R')
    return result


if __name__ == '__main__':
    N, M, S = map(int, input().split())
    char_map = {}
    for i in range(N):
        line = input()
        for j in range(M):
            if line[j] not in char_map:
                char_map[line[j]] = []
            char_map[line[j]].append((i, j))
    # print(char_map)
    id = input()
    id_map = {}
    for c in id:
        if c not in id_map:
            id_map[c] = 1
        else:
            id_map[c] += 1

    strengthen_cnt = None
    for c in id_map:
        if c not in char_map:
            strengthen_cnt = 0
            break

        temp = len(char_map[c]) // id_map[c]
        strengthen_cnt = min(strengthen_cnt, temp) if strengthen_cnt is not None else temp

    print(strengthen_cnt, end=" ")
    path_list = []
    _curr = (0, 0)
    copy_s = strengthen_cnt
    while strengthen_cnt > 0:
        for c in id:
            if _curr in char_map[c]:
                char_map[c].remove(_curr)
                # print('{} : {} -> {}'.format(c, _curr, _curr))
                continue
            _next = char_map[c].pop()
            # print('{} : {} -> {}'.format(c, _curr, _next))
            newly_added = find_route(_curr, _next)
            path_list.extend(newly_added)
            _curr = _next
            # print('path_list : {}'.format(path_list))
            # print(char_map)
        path_list.append('P')
        # print('path_list : {}'.format(path_list))
        strengthen_cnt -= 1
    last = find_route(_curr, (N-1, M-1))
    path_list.extend(last)
    print(len(path_list))
    print(''.join(path_list))