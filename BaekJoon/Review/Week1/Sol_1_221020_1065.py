"""
https://www.acmicpc.net/problem/1065
"""

if __name__ == '__main__':
    N = int(input())



    if N < 100:
        result = N
    else:
        result = 99
        for i in range(100, N+1):
            if i == 1000:
                break
            a, b, c = i % 10, (i % 100) // 10, i // 100
            if a-b == b-c:
                result += 1

    print(result)