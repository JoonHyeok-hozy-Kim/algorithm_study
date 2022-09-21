"""
2866. 문자열 잘라내기
https://www.acmicpc.net/problem/2866
"""

from itertools import combinations
def convert_matrix(matrix, rownum, colnum):
    result = [[] for i in range(colnum)]
    for row in range(rownum-1):
        for col in range(colnum):
            result[col].append(matrix[row+1][col])
    for i in range(len(result)):
        result[i] = ''.join(result[i])
    return result

def counter(converted_mat, l):
    comb_set = combinations(converted_mat, 2)
    min_count = l
    # print('l : {}'.format(l))
    for comb in comb_set:
        temp_count = l
        # print('{}-{}'.format(comb[0], comb[1]))
        for i in range(l):
            # print(' -> {} vs {}'.format(comb[0][l-1-i], comb[1][l-1-i]))
            if comb[0][l-1-i] == comb[1][l-1-i]:
                # print(' ----> FOUND')
                temp_count -= 1
            else:
                break
        min_count = min(min_count, temp_count)
    return min_count

if __name__ == '__main__':
    row_num, col_num = map(int, input().split())
    if col_num in (0, 1):
        print(0)
    else:
        string_matrix = []
        for row in range(row_num):
            string_matrix.append(input())
        converted_matrix = convert_matrix(string_matrix, row_num, col_num)
        print(counter(converted_matrix, row_num-1))


