"""
https://www.acmicpc.net/problem/1027
"""

def calculate_slope(towers, high, low):
    return (towers[high] - towers[low]) / (high - low)


if __name__ == '__main__':
    N = int(input())
    towers = list(map(int, input().split()))

    # print(towers)
    visible_map = {}
    for i in range(N):
        visible_map[i] = []

    for i in range(N):
        min_slope = None
        for j in range(i+1, N):
            curr_slope = calculate_slope(towers, i, j)
            if min_slope is None or curr_slope > min_slope:
                visible_map[i].append(j)
                visible_map[j].append(i)
                min_slope = curr_slope

    # print(visible_map)
    max_cnt = 0
    for k in visible_map:
        max_cnt = max(max_cnt, len(visible_map[k]))
    print(max_cnt)



