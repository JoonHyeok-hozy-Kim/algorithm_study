"""
https://www.acmicpc.net/problem/2503
"""


def validate(num1_list, num2_list, K, B):
    K_cnt = B_cnt = 0
    for i in range(3):
        if num1_list[i] == num2_list[i]:
            K_cnt += 1
        elif num1_list[i] == num2_list[(i+1)%3] or num1_list[i] == num2_list[(i+2)%3]:
            B_cnt += 1
    if K == K_cnt and B == B_cnt:
        return True
    return False


def filter_candidates(C):
    called_num, strikes, balls = map(int, input().split())
    # print(called_num, strikes, balls)
    called_num_list = list(str(called_num))

    filtered = []
    for cand_num in C:
        cand_num_list = list(str(cand_num))
        if validate(called_num_list, cand_num_list, strikes, balls):
            filtered.append(cand_num)

    return filtered


if __name__ == '__main__':
    N = int(input())
    candidates = []
    for i in range(123, 988):
        s = str(i)
        if s[0] == s[1] or s[0] == s[2] or s[1] == s[2]:
            continue
        if s[0] == '0' or s[1] == '0' or s[2] == '0':
            continue
        candidates.append(i)
    # print(candidates)

    for _ in range(N):
        candidates = filter_candidates(candidates)
    print(len(candidates))