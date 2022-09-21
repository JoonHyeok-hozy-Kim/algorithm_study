"""
2309. 일곱 난쟁이
https://www.acmicpc.net/problem/2309
"""

from itertools import combinations
def comb_and_find(L):
    comb_set = combinations(L, 7)
    for x in comb_set:
        sum = 0
        for i in x:
            sum += i
            if sum > 100:
                break
        if sum == 100:
            result = list(x)
            result.sort()
            return result


if __name__ == '__main__':
    dwarves_list = []
    for i in range(9):
        dwarves_list.append(int(input()))
    for dwarf in comb_and_find(dwarves_list):
        print(dwarf)