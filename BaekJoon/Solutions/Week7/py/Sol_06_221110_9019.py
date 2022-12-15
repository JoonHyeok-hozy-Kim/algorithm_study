"""
https://www.acmicpc.net/problem/9019
"""
from collections import deque
from copy import deepcopy


def D_operation(S):
    num = S[0]
    record = S[1]
    num *= 2
    num %= 10000
    record.append('D')
    return [num, record]


def S_operation(S):
    num = S[0]
    record = S[1]
    if num == 0:
        num = 9999
    else:
        num -= 1
    record.append('S')
    return [num, record]


def L_operation(S):
    num = S[0]
    record = S[1]
    f = num // 1000
    num *= 10
    num %= 10000
    num += f
    record.append('L')
    return [num, record]


def R_operation(S):
    num = S[0]
    record = S[1]
    l = num % 10
    num //= 10
    num += l * 1000
    record.append('R')
    return [num, record]


def S_validate(L):
    if len(L) < 9999:
        return True
    for i in range(9999):
        if L[len(L)-1-i] != 'S':
            return True
    return False


def L_validate(L):
    if len(L) >= 1 and L[-1] == 'R':
        return False
    if len(L) < 3:
        return True
    for i in range(3):
        if L[len(L)-1-i] != 'L':
            return True
    return False


def R_validate(L):
    if len(L) >= 1 and L[-1] == 'L':
        return False
    if len(L) < 3:
        return True
    for i in range(3):
        if L[len(L)-1-i] != 'R':
            return True
    return False


def play(A, B):
    target = [A, []]
    Q = deque()
    Q.append(target)
    while len(Q) > 0:
        popped = Q.popleft()
        for i in range(4):
            copied = deepcopy(popped)
            if i%4 == 0:
                temp = D_operation(copied)
            elif i%4 == 1:
                # if not S_validate(copied[1]):
                #     continue
                temp = S_operation(copied)
            elif i%4 == 2:
                if not L_validate(copied[1]):
                    continue
                temp = L_operation(copied)
            else:
                if not R_validate(copied[1]):
                    continue
                temp = R_operation(copied)

            if temp[0] == B:
                return ''.join(temp[1])
            else:
                Q.append(temp)

            # print(Q)


def D_simple(num):
    num *= 2
    num %= 10000
    return num


def S_simple(num):
    if num == 0:
        num = 9999
    else:
        num -= 1
    return num


def L_simple(num):
    f = num // 1000
    num *= 10
    num %= 10000
    num += f
    return num


def R_simple(num):
    l = num % 10
    num //= 10
    num += l * 1000
    return num



def play_with_dp(A, B):
    Q = deque()
    Q.append(A)
    dp = [None] * 10000
    dp[A] = ''
    idx = A
    while idx != B:
        for i in range(4):
            if i%4 == 0:
                new, alpha = D_simple(idx), 'D'
            elif i%4 == 1:
                new, alpha = S_simple(idx), 'S'
            elif i%4 == 2:
                new, alpha = L_simple(idx), 'L'
            else:
                new, alpha = R_simple(idx), 'R'

            if dp[new] is None:
                new_text = dp[idx] + alpha

                if new == B:
                    return new_text
                else:
                    dp[new] = new_text
                    Q.append(new)

        # print(dp)
        idx = Q.popleft()

    return dp[idx]


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        # result = play(A, B)
        result = play_with_dp(A, B)
        print(result)