"""
https://www.acmicpc.net/problem/26111
"""
# import sys
# sys.setrecursionlimit(10**7)


def parse_text(T, i=0, d=0, cnt=0):
    if i == len(T):
        # print('final, i : {}, d : {}, cnt : {}'.format(i, d, cnt))
        return cnt
    # print('i : {}, d : {}, cnt : {}'.format(i, d, cnt))
    if T[i] == '(':
        return parse_text(T, i+1, d+1, cnt)
    elif T[i] == ')':
        # print('ADD, d-1 : {}'.format(d-1))
        if T[i-1] == '(':
            return parse_text(T, i+1, d-1, cnt+(d-1))
        else:
            return parse_text(T, i+1, d-1, cnt)


def parse_text_with_stack(T):
    depth = 0
    cnt = 0
    for i in range(len(T)):
        if T[i] == '(':
            depth += 1
        elif T[i] == ')':
            if T[i-1] == '(':
                cnt += depth - 1
            depth -= 1
    return cnt



if __name__ == '__main__':
    text = input()
    # print(parse_text(text))
    print(parse_text_with_stack(text))