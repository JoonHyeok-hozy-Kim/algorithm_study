"""
2628. 종이자르기
https://www.acmicpc.net/problem/2628
"""

def longest(max_length, cut_list):
    points_list = [0]
    for point in cut_list:
        points_list.append(point)
    points_list.append(max_length)
    delta = 0
    for i in range(len(points_list)-1):
        delta = max(delta, points_list[i+1] - points_list[i])
    return delta

if __name__ == "__main__":
    width, height = map(int, input().split())
    cut_times = int(input())
    cut_map = {'horizontal': [], 'vertical': []}
    for i in range(cut_times):
        direction, num = map(int, input().split())
        if direction == 0:
            cut_map['horizontal'].append(num)
        else:
            cut_map['vertical'].append(num)

    cut_map['horizontal'].sort()
    cut_map['vertical'].sort()
    result = longest(height, cut_map['horizontal']) * longest(width, cut_map['vertical'])
    print(result)
