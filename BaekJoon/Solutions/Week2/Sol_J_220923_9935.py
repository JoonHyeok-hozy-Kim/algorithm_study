"""
9935. 문자열 폭발
https://www.acmicpc.net/problem/9935
"""
from collections import deque

def find_and_explode(T, E):
    S = deque()
    while len(T) > 0:
        S.append(T.popleft())
        i = -1
        while S[i] == E[i] and len(S) >= len(E):
            if i*(-1) == len(E):
                for _ in range(len(E)):
                    S.pop()
                break
            i -= 1
    return S

if __name__ == '__main__':
    text = deque(input())
    explosion = input()
    s = find_and_explode(text, explosion)
    result = ''.join(s) if len(s) > 0 else 'FRULA'
    print(result)





