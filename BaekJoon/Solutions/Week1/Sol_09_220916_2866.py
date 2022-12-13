"""
2866. 문자열 잘라내기
https://www.acmicpc.net/problem/2866
"""

def create_map_and_cnt(_str_map, _C, _R, _strings, i, j=None, _curr_cnt=0):
    if j is None:
        j = _R-1

    if j < 0:
        return _curr_cnt

    if _strings[j][i] in _str_map:
        return create_map_and_cnt(_str_map[_strings[j][i]], _C, _R, _strings, i, j-1, _curr_cnt+1)
    else:
        _str_map[_strings[j][i]] = {}
        return create_map_and_cnt(_str_map[_strings[j][i]], _C, _R, _strings, i, j-1, _curr_cnt)

if __name__ == '__main__':
    R, C = map(int, input().split())
    strings = [None] * R
    for i in range(R):
        strings[i] = input()

    str_map = {}
    max_cnt = 0

    for i in range(C):
        max_cnt = max(max_cnt, create_map_and_cnt(str_map, C, R, strings, i))
        # print(max_cnt, str_map)
    print(R-max_cnt-1)