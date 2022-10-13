"""
2437. 저울
https://www.acmicpc.net/problem/2437
"""


if __name__ == '__main__':
    N = int(input())
    bells = list(map(int, input().split()))

    bells.sort()
    dp = [0] * bells[0]
    dp[bells[0]-1] = 1

    end_flag = False
    for i in range(N-1):
        # print(dp)
        for j in range(len(dp)):
            if dp[j] == 0:
                print(j+1)
                end_flag = True
                break
        if end_flag:
            # print('B')
            break

        for _ in range(bells[i+1]):
            dp.append(0)
        dp[bells[i+1]-1] = 1

        for j in range(len(dp)):
            if dp[j] > 0 and j+bells[i+1] < len(dp):
                dp[j+bells[i+1]] = dp[j]

    if not end_flag:
        for j in range(len(dp)):
            if dp[j] == 0:
                print(j+1)
                end_flag = True
                break

    if not end_flag:
        print(sum(bells)+1)