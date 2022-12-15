"""
2262. 기업투자
https://www.acmicpc.net/problem/2662
"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    returns_list = [None] * (N+1)
    for i in range(N):
        temp_return = list(map(int, input().split()))
        invest_amt = temp_return[0]
        temp_return[0] = 0      # Imaginary first firm with ZERO return!
        returns_list[invest_amt] = temp_return
    # print(returns_list)

    dp = [[0] * (N+1) for _ in range(M+1)]
    path = [[0] * (N+1) for _ in range(M+1)]
    for i in range(1, M+1):
        # print('\n[LOOP1] i : {}'.format(i))
        for total_inv in range(1, N+1):
            # print(' [LOOP2] total_inv : {}'.format(total_inv))
            dp[i][total_inv] = dp[i-1][total_inv]
            for curr_inv in range(1, total_inv+1):
                # print('  [LOOP3] curr_inv : {}'.format(curr_inv))
                val = dp[i-1][total_inv-curr_inv] + returns_list[curr_inv][i]
                if val > dp[i][total_inv]:
                    dp[i][total_inv] = val
                    path[i][total_inv] = curr_inv
    #             print('dp   : {}\npath : {}'.format(dp, path))
    # print('dp   : {}\npath : {}'.format(dp, path))

    print(dp[M][N])
    m, n = M, N
    result = []
    while m > 0:
        v = path[m][n]
        # print('m : {}, n : {}, val : {}'.format(m, n, v))
        result.append(str(v))
        n -= v
        m -= 1
    print(' '.join(reversed(result)))

