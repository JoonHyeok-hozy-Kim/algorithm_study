"""
1027. 고층 건물
https://www.acmicpc.net/problem/1027
"""

def visible_buildings_count(buildings, n):
    # left side
    result = 0
    left_slope = None
    for i in range(n):
        temp_slope = (buildings[n] - buildings[n-1-i]) / (i+1)
        if left_slope is None or temp_slope < left_slope:
            result += 1
            left_slope = temp_slope

    right_slope = None
    for j in range(len(buildings)-n-1):
        temp_slope = (buildings[n+1+j] - buildings[n]) / (j+1)
        if right_slope is None or temp_slope > right_slope:
            result += 1
            right_slope = temp_slope

    return result


if __name__ == '__main__':
    N = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(N):
        result = max(visible_buildings_count(buildings, i), result)
    print(result)

