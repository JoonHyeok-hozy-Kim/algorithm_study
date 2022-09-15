'''
1448 삼각형 만들기

세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의
최댓값을 구하고 싶다.
'''


# Using combinations : Failed.
from itertools import combinations
def triangle_test(set):
    max_val = set[0]
    rest = []
    for i in range(1,3):
        if set[i] > max_val:
            rest.append(max_val)
            max_val = set[i]
        else:
            rest.append(set[i])
    rest_sum = sum(rest)
    return rest_sum + max_val if rest_sum > max_val else -1

def comb_test(L):
    comb_set = combinations(L, 3)
    result = -1
    for x in comb_set:
        test_result = triangle_test(x)
        result = max(result, test_result)
    return result


# Case division : Success
def new_triangle_test(sorted_set):
    part_sum = sorted_set[0] + sorted_set[1]
    return part_sum + sorted_set[2] if part_sum > sorted_set[2] else -1

def new_item_test(t_set, current, new_item):
    temp_set = t_set
    temp_result = current
    for i in range(3):
        if t_set[(i+1)%3] + t_set[(i+2)%3] + new_item > temp_result:
            new_set = [t_set[(i+1)%3], t_set[(i+2)%3], new_item]
            new_set.sort()
            new_result = new_triangle_test(new_set)
            if new_result > temp_result:
                temp_set = new_set
                temp_result = new_result
    return temp_set, temp_result

def total_test(L, N):
    t_set = [L[0], L[1], L[2]]
    t_set.sort()
    result = new_triangle_test(t_set)
    for i in range(3, N):
        t_set, result = new_item_test(t_set, result, L[i])
    return result

if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        L.append(int(input()))
    print(total_test(L, N))