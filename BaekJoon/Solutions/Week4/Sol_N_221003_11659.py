"""
11659. 구간 합 구하기 4
https://www.acmicpc.net/problem/11659
"""




if __name__ == '__main__':
    N, M = map(int, input().split())


    X = map(int, input().split())
    temp_sum = 0
    sums = [None] * N
    idx = 0
    for x in X:
        temp_sum += x
        sums[idx] = temp_sum
        idx += 1


    for _ in range(M):
        i, j = map(int, input().split())
        print(sums[j-1]-sums[i-2]) if i > 1 else print(sums[j-1])