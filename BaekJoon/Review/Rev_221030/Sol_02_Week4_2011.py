"""
https://www.acmicpc.net/group/practice/view/15665/4
"""

import sys
sys.setrecursionlimit(10**6)


def recursive_parse(N, cnt=0):
    if cnt == len(N):
        # print('ADDED')
        return 1
    elif cnt > len(N):
        return 0

    result = 0
    if int(N[cnt]) == 1:
        if cnt < int(len(N))-1 and int(N[cnt + 1]) == 0:
            result += recursive_parse(N, cnt + 2)

        else:
            result += recursive_parse(N, cnt+1)
            result += recursive_parse(N, cnt+2)


    elif int(N[cnt]) == 2:
        if cnt < int(len(N))-1 and int(N[cnt+1]) == 0:
            result += recursive_parse(N, cnt+2)

        elif cnt < int(len(N))-1 and int(N[cnt+1]) <= 6:
            result += recursive_parse(N, cnt+1)
            result += recursive_parse(N, cnt+2)

        else:
            result += recursive_parse(N, cnt+1)

    else:
        result += recursive_parse(N, cnt+1)

    return result


def get_fibo_list(n):
    result = []
    result.append(1)
    if n == 1:
        return result
    result.append(2)
    if n == 2:
        return result

    for i in range(n-2):
        val = result[-1] + result[-2]
        result.append(val)
    return result


def get_partition(N):
    P = []
    start = 0
    for i in range(1, len(N)):
        # print(i)
        if start >= len(N):
            break

        if N[i-1] == '1':
            if N[i] in ('1', '2'):
                # print('pt1-1')
                continue

            elif N[i] == '0':
                # print('pt1-2')
                P.append(i - start)
                start = i+2

            else:
                # print('pt1-3')
                P.append(i-start+1)
                start = i+2

        elif N[i-1] == '2':
            if N[i] in ('1', '2'):
                # print('pt2-1')
                continue

            elif int(N[i]) <= 6:
                # print('pt2-2')
                P.append(i-start+1)
                start = i+2

            elif N[i] == '0':
                # print('pt2-3')
                P.append(i - start)
                start = i+2

            else:
                # print('pt2-4')
                P.append(i - start)
                start = i+1

        else:
            if N[i] in ('1', '2'):
                # print('pt3-1')
                P.append(i - start -1)
                start = i

            else:
                # print('pt3-2')
                P.append(i - start)
                start = i+1

        # print(P)

    if start < len(N):
        P.append(len(N)-start)
    # print(P)

    return P


if __name__ == '__main__':
    N = input()

    # result = recursive_parse(N)

    P = get_partition(N)
    m = max(P)
    F = get_fibo_list(m)
    result = 1
    for i in range(len(P)):
        if P[i] > 0:
            result *= F[P[i]-1]

    print(result%1000000)