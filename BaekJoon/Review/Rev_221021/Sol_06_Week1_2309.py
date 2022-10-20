"""
https://www.acmicpc.net/problem/2309
"""

def solution(D):
    target = sum(D) - 100
    # print(target)

    for i in range(9):
        for j in range(i+1, 9):
            if D[i] + D[j] == target:
                return i, j


if __name__ == '__main__':
    dwarves = [int(input()) for _ in range(9)]
    dwarves.sort()
    # print(dwarves)

    reject = solution(dwarves)
    for k in range(9):
        if k not in reject:
            print(dwarves[k])