"""
2011. 암호코드
https://www.acmicpc.net/problem/2011
"""

def get_counting_list(n):
    L = [None] * n
    L[0] = 1
    if n == 1:
        return L
    L[1] = 2
    if n == 2:
        return L

    for i in range(2, n):
        temp = L[i-2] + L[i-1]
        if temp > 1000000:
            temp %= 1000000
        L[i] = temp

    return L


def trim_zero_in_str(S):
    LS = []
    for i in S:
        if i != '0':
            LS.append(i)
    return ''.join(LS)


def count_possible_ciphers(S):

    valid_partition = []
    prev_i = -1
    zero_cnt = 0
    for i in range(len(S)):
        if S[i] == '0' and i > 0 and S[i-1] in ('1', '2'):
            temp_partition = S[prev_i+1:i-1]
            if temp_partition != '':
                if '0' in temp_partition:
                    return 0
                valid_partition.append(temp_partition)
            prev_i = i
            zero_cnt += 1
    if prev_i != len(S)-1:
        temp_partition = S[prev_i+1:]
        if '0' in temp_partition:
            return 0
        valid_partition.append(temp_partition)

    # print(valid_partition)
    if len(valid_partition) == 0:
        return 1

    group_in_partitions = []
    max_val = None
    for P in valid_partition:
        count_by_group = []
        temp_cnt = 0
        for i in range(len(P)):
            if P[i] in ('1', '2'):
                temp_cnt += 1
            else:
                if temp_cnt > 0:
                    if int(P[i-1]) == 1 or int(P[i]) <= 6:
                        temp_cnt += 1
                    count_by_group.append(temp_cnt)
                    temp_cnt = 0
                else:
                    count_by_group.append(1)
        if temp_cnt > 0:
            count_by_group.append(temp_cnt)

        max_val = max(max_val, max(count_by_group)) if max_val is not None else max(count_by_group)
        group_in_partitions.append(count_by_group)



    comb_set = get_counting_list(max_val)
    # print(comb_set)
    # print(group_in_partitions)
    final = 1
    for G in group_in_partitions:
        # print(G)
        for k in G:
            final *= comb_set[k-1]
    return final % 1000000



if __name__ == '__main__':
    S = input().rstrip()
    print(count_possible_ciphers(S))

    # while True:
    #     test_case = input().rstrip()
    #     if test_case == -1:
    #         break
    #     else:
    #         answer = int(input().split()[1])
    #         input()
    #         x = count_possible_ciphers(test_case)
    #         if answer != x:
    #             print('test_case : {}, answer : {}, mine : {}'.format(test_case, answer, x))
