"""
https://www.acmicpc.net/problem/1476
"""

def get_esm(E, S, M):
    temp = S
    while True:
        e = temp % 15
        m = temp % 19
        if ((E % 15 == e == 0) or (0 < e == E)) and ((M % 19 == m == 0) or (0 < m == M)):
            return temp
        else:
            temp += 28


if __name__ == '__main__':
    E, S, M = map(int, input().split())
    print(get_esm(E, S, M))