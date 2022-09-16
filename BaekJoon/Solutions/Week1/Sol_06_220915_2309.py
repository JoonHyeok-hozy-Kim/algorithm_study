"""
2309. 일곱 난쟁이

왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉
명이었던 것이다.
아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는,
다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
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