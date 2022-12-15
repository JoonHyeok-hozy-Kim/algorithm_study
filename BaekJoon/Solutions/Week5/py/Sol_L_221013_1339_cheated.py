"""
1339. 단어 수학
https://www.acmicpc.net/problem/1339
"""


if __name__ == '__main__':
    N = int(input())
    words = [input() for _ in range(N)]
    alpha_num = {}
    nums = [i for i in range(10)]

    for w in words:
        power = 1
        for j in range(len(w)):
            A = w[len(w)-j-1]
            if A not in alpha_num:
                alpha_num[A] = 0
            alpha_num[A] += power
            power *= 10

    rank_by_usage = [(alpha_num[key], key) for key in alpha_num.keys()]
    rank_by_usage.sort(reverse=True)
    for x in rank_by_usage:
        alpha_num[x[1]] = nums.pop()

    result = 0
    for w in words:
        temp = 0
        power = 1
        for j in range(len(w)):
            A = w[len(w)-j-1]
            temp += alpha_num[A] * power
            power *= 10
        # print(temp)
        result += temp
    print(result)