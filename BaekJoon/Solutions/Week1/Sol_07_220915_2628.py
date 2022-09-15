"""
2628. 종이자르기

점선을 따라 이 종이를 칼로 자르려고 한다. 가로 점선을 따라 자르는 경우는 종이의 왼쪽 끝에서 오른쪽 끝까지, 세로 점선인 경우는 위쪽 끝에서
아래쪽 끝까지 한 번에 자른다. 예를 들어, <그림 1>의 가로 길이 10㎝이고 세로 길이 8㎝인 종이를 3번 가로 점선, 4번 세로 점선, 그리고 2번
가로 점선을 따라 자르면 <그림 2>와 같이 여러 개의 종이 조각으로 나뉘게 된다. 이때 가장 큰 종이 조각의 넓이는 30㎠이다.
입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오.
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
