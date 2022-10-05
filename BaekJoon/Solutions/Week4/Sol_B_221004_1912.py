"""
1912. 연속합
https://www.acmicpc.net/problem/1912
"""


if __name__ == '__main__':
    N = int(input())
    partial_sum_list = []
    temp_max = None

    cnt = 0
    for i in map(int, input().split()):
        if cnt == 0:
            partial_sum_list.append(i)
            temp_max = i

        else:
            temp_val = i
            if partial_sum_list[cnt-1] > 0:
                temp_val += partial_sum_list[cnt-1]
            partial_sum_list.append(temp_val)

            if temp_val > temp_max:
                temp_max = temp_val

        cnt += 1
        # print(partial_sum_list)

    print(temp_max)
