"""
1339. 단어 수학
https://www.acmicpc.net/problem/1339
"""


if __name__ == '__main__':
    N = int(input())
    words = [[None, 0, input()] for _ in range(N)]
    alpha_num = {}
    nums = [i for i in range(10)]

    for w in words:
        w[0] = len(w[2])

    words.sort(reverse=True)
    # print(words)

    idx = 0
    curr_digit = words[0][0]
    while curr_digit >= 0:
        if len(nums) == 0:
            break

        candidates = []
        for s in words:
            if 0 < s[0] - s[1] == curr_digit:
                A = s[2][s[1]]
                if A not in alpha_num:
                    not_included = True
                    for x in candidates:
                        if x[1] == A:
                            x[0] += 1
                            not_included = False
                            break
                    if not_included:
                        candidates.append([1, A])
                # print(s[2], A, candidates)
                s[1] += 1

        candidates.sort(reverse=True)
        for x in candidates:
            if x[1] not in alpha_num:
                alpha_num[x[1]] = nums.pop()
                print(x[1], alpha_num[x[1]])

        curr_digit -= 1

    result = 0
    for s in words:
        temp = 0
        power = 1
        for j in range(s[0]):
            temp += alpha_num[s[2][s[0]-j-1]] * power
            power *= 10
        print(temp)
        result += temp
    print(result)
