"""
25494. 단순한 문제 (Small)

https://www.acmicpc.net/problem/25494
"""


def get_int_set_count(int_set):
    result = 0
    for x in range(1, int_set[0]+1):
        for y in range(1, int_set[1]+1):
            for z in range(1, int_set[2]+1):
                if x % y == y % z == z % x:
                    result += 1
    return result


if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        int_set = list(map(int, input().split()))
        print(get_int_set_count(int_set))