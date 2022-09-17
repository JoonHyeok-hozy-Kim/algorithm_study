"""
11651. 좌표 정렬하기 2

2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""


def point_comes_first(p1, p2):
    # y-coordinate increasing order
    if p1[1] < p2[1]:
        return True
    elif p1[1] == p2[1] and p1[0] < p2[0]:
        return True
    return False


def _merge_array(S, S1, S2):
    one_idx = two_idx = 0
    while one_idx + two_idx < len(S):
        if two_idx == len(S2) or (one_idx < len(S1) and point_comes_first(S1[one_idx], S2[two_idx])):
            S[one_idx + two_idx] = S1[one_idx]
            one_idx += 1
        else:
            S[one_idx + two_idx] = S2[two_idx]
            two_idx += 1
    return


def merge_sort_points(S):
    n = len(S)
    if n <= 1:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]

    merge_sort_points(S1)
    merge_sort_points(S2)
    _merge_array(S, S1, S2)
    return


if __name__ == '__main__':
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))

    merge_sort_points(points)
    for point in points:
        print('{} {}'.format(point[0], point[1]))