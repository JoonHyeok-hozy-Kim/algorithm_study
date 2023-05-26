# https://www.acmicpc.net/problem/1013
import re

def recursive_validation(S):
    i = 0
    if S[i] == '0':
        return second(S, i)
    elif S[i] == '1':
        return first(S, i)
    else:
        return False

def first(S, i, depth=0):
    # print(' '*depth, end="")
    # print('first(), i : {}'.format(i))
    if S[i] != '1': return False
    else: i += 1

    if i == len(S) or S[i] != '0': return False
    else: i += 1

    if i == len(S) or S[i] != '0': return False
    else: i += 1

    while i < len(S) and S[i] == '0':
        i += 1
    
    if i == len(S) or S[i] != '1': return False
    else: i += 1

    while i < len(S) and S[i] == '1':
        if first(S, i, depth+1):
            return True
        i += 1
    
    if i == len(S):
        return True
    elif S[i] == '0' and second(S, i, depth+1):
        return True
    else:
        return False
    

def second(S, i, depth=0):
    # print(' '*depth, end="")
    # print('second(), i : {}'.format(i))
    while i < len(S) and S[i] == '0':
        i += 1

        if i == len(S) or S[i] != '1': return False
        else: i += 1
    
    if i == len(S):
        return True
    elif S[i] == '1':
        return first(S, i, depth+1)
    else:
        return False


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        if recursive_validation(input()):
            print('YES')
        else:
            print('NO')