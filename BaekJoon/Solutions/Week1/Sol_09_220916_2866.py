"""
2866. 문자열 잘라내기

R개의 행과 C개의 열로 이루어진 테이블이 입력으로 주어진다. 이 테이블의 원소는 알파벳 소문자이다.

각 테이블의 열을 위에서 아래로 읽어서 하나의 문자열을 만들 수 있다. 예제 입력에서

dobarz
adatak
이 주어지는 경우 "da", "od", "ba", "at", "ra", "zk"와 같이 6개의 문자열들이 만들어지게 된다.

만약 가장 위의 행을 지워도 테이블의 열을 읽어서 문자열이 중복되지 않는다면, 가장 위의 행을 지워주고, count의 개수를 1 증가시키는,
이 과정을 반복한다. 만약 동일한 문자열이 발견되는 경우, 반복을 멈추고 count의 개수를 출력 후 프로그램을 종료한다.

테이블이 주어질 경우 count의 값을 구해보자.
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


