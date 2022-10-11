"""
1947. 선물 전달
https://www.acmicpc.net/problem/1947
"""


if __name__ == '__main__':
    N = int(input())
    result_list = [0, 1]
    if N <= 2:
        print(result_list[N-1])
    else:
        for i in range(3, N+1):
            val = ((i-1)*result_list[i-3] % 1000000000 + (i-1)*result_list[i-2] % 1000000000) % 1000000000
            result_list.append(val)
        print(result_list[-1])