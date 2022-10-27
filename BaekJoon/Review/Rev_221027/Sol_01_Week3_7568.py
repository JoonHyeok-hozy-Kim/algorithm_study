"""
https://www.acmicpc.net/problem/7568
"""


if __name__ == '__main__':
    N = int(input())
    specs = [list(map(int, input().split())) for _ in range(N)]
    # print(specs)

    one_to_one = {}
    for i in range(N):
        one_to_one[i] = []
        for j in range(N):
            if i != j:
                if specs[j][0] > specs[i][0] and specs[j][1] > specs[i][1]:
                    one_to_one[i].append(j)
    # print(one_to_one)

    result = []
    for k in one_to_one.keys():
        result.append([k, len(one_to_one[k])])
    # print(result)

    result.sort()
    # print(result)

    for i in result:
        print(i[1]+1, end=" ")