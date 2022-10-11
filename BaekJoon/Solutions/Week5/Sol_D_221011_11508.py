"""
11508. 2+1 세일
https://www.acmicpc.net/problem/11508
"""


if __name__ == '__main__':
    N = int(input())
    dairies = [int(input()) for _ in range(N)]
    # print(dairies)
    dairies.sort()

    j = N // 3

    result = 0
    while len(dairies) >= 3:
        result += dairies.pop() + dairies.pop()
        dairies.pop()

    for d in dairies:
        result += d

    print(result)


    # 4 5 5 5 5 6